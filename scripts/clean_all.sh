 #!/bin/sh

########################################################

## Shell Script to Clean Network
## Stop Dockers and Remove Dockers

########################################################



echo "Stopping all dockers, takes a bit be patient"
docker stop $(docker ps -a -q)

echo "Removing all docker containers"
docker rm $(docker ps -a -q)

echo "Removing all docker images"
docker rmi -f $(docker images -aq)

echo "Removing microservices network"
sudo docker network rm microservices

echo "CLEAN COMPLETE"
#Chamar Docker Compose
#O shell poe no docker desktop o docker file
