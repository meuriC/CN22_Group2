 printf "Building Docker Network first\n"

{ sudo docker network create microservices
} &> /dev/null


printf "\t Running Games"
sudo docker run -p 127.0.0.1:50051:50051/tcp games --network="microservices" --name "games" &
printf "done\n"

printf "\t Running Games"
sudo docker run -p 127.0.0.1:50055:50055/tcp account --network="microservices" --name "games" &
printf "done\n"