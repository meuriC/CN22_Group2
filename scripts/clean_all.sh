 #!/bin/sh

########################################################

## Shell Script to Clean Network
## Stop Dockers and Remove Dockers

########################################################



echo "Stopping all dockers, takes a bit be patient"
docker stop $(docker ps -a -q)

echo "Removing all dockers"
docker rm $(docker ps -a -q)

echo "Removing microservices network"
sudo docker network rm microservices

echo "CLEAN COMPLETE"
#Chamar Docker Compose
#O shell poe no docker desktop o docker file
