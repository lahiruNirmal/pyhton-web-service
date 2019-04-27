# pyhton-web-service using docker containers for automated deployment

## Prerequisites

  1. Your machine must be installed with Docker.
  2. You must be logged into your a docker hub account registry for pulling base docker images.

## Deployment

  1. Execute start.sh to deploy python Rest-api service and mysql docker containers.
  2. Check the status of the docker containers using "docker ps" command.
  3. Interact with the Rest-api using Postman or curl commands.

### EXAMPLES:

#### Get all users in the table
  curl -X GET http://localhost:8080/users
#### Insert a user to the table 
  curl -d '{"fullName":"Lahiru Wijesuriya", "userName":"lahiru", "tenantId":1}' -H "Content-Type: application/json" -X POST localhost:8080/insert
#### Update a user in the table - curl -d _tenantId=1 -d _userName=lahiru -G localhost:8080/user/
  curl -d '{"fullName":"Lahiru Wijesuriya_1", "userName":"lahiru_2", "tenantId":5}' -H "Content-Type: application/json" -X POST localhost:8080/update
