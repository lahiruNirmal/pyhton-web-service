# -----------Created by Lahiru Wijesuriya-------------
from app import app
from flaskext.mysql import MySQL
import os

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'test-db'
app.config['MYSQL_DATABASE_HOST'] = os.environ['MYSQL_DATABASE_HOST']
mysql.init_app(app)