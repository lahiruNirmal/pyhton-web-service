FROM python:2.7-slim-stretch
RUN apt-get update && apt install -qy apt-utils net-tools
RUN mkdir -p /app/ && pip install Flask pymysql flask-mysql
EXPOSE 80
WORKDIR /app
COPY ./* ./
CMD [ "python", "main.py" ]