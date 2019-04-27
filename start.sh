#!/bin/bash

# Building docker images.
number_of_containers=$(docker ps | grep -i web-service | wc -l)
container_name=$(docker ps | grep -i web-service | awk '{ print $1 }')
image_name=$(docker images | grep -i web-service | awk '{ print $3 }')
current_time_stamp=$(date +"%I%M%S")

if [ $number_of_containers -ge 1 ]; then
    echo "Not first deployment."
    docker container stop $container_name
    docker container rm $container_name
    docker rmi $image_name 
    docker build -t web-service:$current_time_stamp ./python/
    mysql_host=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql)
    docker run -itd -p 8080:8080 -e MYSQL_DATABASE_HOST=$mysql_host --name web-service web-service:$current_time_stamp
else
    echo "First deployment"
    docker build -t mysql:$current_time_stamp ./mysql/
    docker run -itd --name mysql -p 3306:3306 mysql:$current_time_stamp
    mysql_host=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql)
    docker build -t web-service:$current_time_stamp ./python/
    docker run -itd -p 8080:8080 -e MYSQL_DATABASE_HOST=$mysql_host --name web-service web-service:$current_time_stamp
    
fi