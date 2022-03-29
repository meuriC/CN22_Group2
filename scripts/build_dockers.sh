printf "Building Dockers\n" 
printf "\t Building Games" 
{ sudo docker build . -f ../api/microservices/games/Dockerfile -t games
} &> /dev/null 
printf "Games Docker built\n" 
 
printf "\t Building Reviews " 
{ sudo docker built . -f ../api/microservices/reviews/Dockerfile -t reviews
} &> /dev/null 
printf "Reviews Docker built\n" 
 
printf "\t Building Users " 
{ sudo docker build . -f ../api/microservices/reviews/Dockerfile -t reviews
} &> /dev/null 
printf "Users Docker built\n" 
 


# remove protos TODO: Remove protos after proto building is automated
#rm ./app/protobufs/*/*pb2* 
