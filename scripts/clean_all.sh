 #!/bin/sh

########################################################

## Shell Script to Build Docker Image 

########################################################

echo "Removing all unused networks"
sudo docker network prune -y &

echo "Stopping all dockers"
docker stop $(docker ps -a -q) &

echo"Removing all dockers"
docker rm $(docker ps -a -q)

#Chamar Docker Compose
#O shell poe no docker desktop o docker file
