# coding: utf-8


# -----------Created by Lahiru Wijesuriya-------------
import pymysql
from flask import flash, request
from db_configuration import mysql
from flask import jsonify
from app import app
from datetime import datetime
from password_generator import generatePwd 
import string

# Insert a user.
@app.route('/insert', methods=['POST'])
def insertUser():
	try:
		_json = request.json
		_fullName = _json['fullName']
		_userName = _json['userName']
		_tenantId = _json['tenantId']
		_active = True
		_userPassword = generatePwd(12, string.letters)
		_changedTime = datetime.now()
		# _changedTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		print _fullName
		# validate the received values
		if _fullName and _userName and _active and _changedTime and _tenantId and request.method == 'POST':
			sql = "INSERT INTO USER(FULL_NAME, USER_NAME, USER_PASSWORD, ACTIVE, CHANGED_TIME, TENANT_ID) VALUES(%s, %s, %s, %s, %s, %s)"			
			data = (_fullName, _userName, _userPassword, _active, _changedTime, _tenantId)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

# Retreive all users.
@app.route('/users')
def getUsers():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM USER")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

# Retrieve a specific user.
@app.route('/user/')
def getUser():
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	try:
		_tenantId = request.args.get('_tenantId')
		_userName = request.args.get('_userName')
		sql = "SELECT * FROM USER WHERE TENANT_ID=%s AND USER_NAME=%s"
		data = (int(_tenantId), _userName)
		cursor.execute(sql, data)
		row = cursor.fetchall()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

# Update a user.
@app.route('/update', methods=['POST'])
def update_user():
	conn = mysql.connect()
	cursor = conn.cursor()
	try:
		_json = request.json
		_fullName = _json['fullName']
		_userName = _json['userName']
		_tenantId = _json['tenantId']
		_userPassword = generatePwd(12, string.letters)
		_changedTime = datetime.now()

		print _fullName
		# validate the received values
		if _fullName and _userName and _userPassword and _changedTime and _tenantId and request.method == 'POST':
			sql = "UPDATE USER SET FULL_NAME=%s, USER_PASSWORD=%s, CHANGED_TIME=%s WHERE TENANT_ID=%s AND USER_NAME=%s"
			data = (_fullName, _userPassword, _changedTime, _tenantId, _userName)
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

# Error handling
@app.errorhandler(404)
def not_found(error=None):
	message = {
		'status': 404,
		'message': 'Not Found: ' + request.url
	}
	resp = jsonify(message)
	resp.status_code = 404

	return resp

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)