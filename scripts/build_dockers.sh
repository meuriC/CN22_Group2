printf "Building Docker Network first\n"

{ sudo docker network create microservices
} &> /dev/null

printf "changing directory"
cd ../api/microservices

printf "\t Building Games" 
{ sudo docker build . -f games/Dockerfile -t games
} &> /dev/null 
printf "Games Docker built\n" 

 
printf "\t Building Reviews " 
{ sudo docker build . -f reviews/Dockerfile -t reviews
} &> /dev/null 
printf "Reviews Docker built\n" 

printf "\t Building Users " 
{ sudo docker build . -f reviews/Dockerfile -t user
} &> /dev/null 
printf "Users Docker built\n" 
 


# remove protos TODO: Remove protos after proto building is automated
#rm ./app/protobufs/*/*pb2* 
