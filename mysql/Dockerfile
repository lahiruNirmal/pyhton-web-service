# -----------Created by Lahiru Wijesuriya-------------
FROM mysql:5.5.60
ENV MYSQL_DATABASE=test-db
ENV MYSQL_USER=admin
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_PASSWORD=password
EXPOSE 3306
COPY ./bootstrap.sql docker-entrypoint-initdb.d/
RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/