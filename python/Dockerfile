FROM python:3.6
RUN apt-get update && apt install -qy apt-utils net-tools curl
RUN mkdir -p /app/ && pip install Flask pymysql flask-mysql
WORKDIR /app
COPY ./* ./
CMD [ "python", "main.py" ]