########################################################

## Shell Script to Build Network and Docker Images 
## Do this on bash before running the file IF YOU HAVE A "\r" INVALID FORMAT --> sed -i 's/\r//g' create-docker-imgs.sh

########################################################

printf "Building Docker Network first\n"

{ sudo docker network create microservices
} &> /dev/null

printf "Changing directory\n"
cd ../api/microservices

printf "\t Building Games" 
{ sudo docker build . -f games/Dockerfile -t games
} &> /dev/null 
printf " ... done\n" 

printf "\t Building Reviews " 
{ sudo docker build . -f reviews/Dockerfile -t reviews
} &> /dev/null 
printf " ... done\n" 

printf "\t Building Users " 
{ sudo docker build . -f users/Dockerfile -t users
} &> /dev/null 
printf " ... done\n" 

printf "\t Building Steam " 
{ sudo docker build . -f steam/Dockerfile -t steam
} &> /dev/null 
printf " ... done\n" 

printf "\t Building Gateway " 
{ sudo docker build . -f gateway/Dockerfile -t gateway
} &> /dev/null 
printf " ... done\n"

printf "\t Building Containers with compose" 
sudo docker-compose up

# remove protos TODO: Remove protos after proto building is automated
#rm ./app/protobufs/*/*pb2* 
