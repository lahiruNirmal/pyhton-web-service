# -----------Created by Lahiru Wijesuriya-------------
FROM python:2.7-slim-stretch
RUN apt-get update && apt install -qy apt-utils net-tools
RUN mkdir -p /app/ && pip install Flask pymysql flask-mysql
WORKDIR /app
COPY ./* ./
CMD [ "python", "main.py" ]