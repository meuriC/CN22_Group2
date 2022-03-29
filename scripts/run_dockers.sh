 printf "Building Docker Network first\n"

{ sudo docker network create microservices
} &> /dev/null


#printf "\t Running Games"
#sudo docker run -p 127.0.0.1:50051:50051/tcp games --network="microservices" --name "games" &
#printf "done\n"


printf "\t Running Users"
sudo docker run -p 127.0.0.1:50052:50052/tcp games --network="microservices" --name "users" &
printf "done\n"

printf "\t Running Reviews"
sudo  docker run -p 127.0.0.1:50051:50051/tcp reviews --network="microservices" --name "reviews" 
printf "done\n"