########################################################

## Shell Script to Run Docker Images 

########################################################

printf "\t Running Users"
sudo docker run -p 127.0.0.1:50052:50052/tcp --network microservices --name users users &
printf "done\n"

printf "\t Running Reviews"
sudo  docker run -p 127.0.0.1:50053:50053/tcp --network microservices --name reviews reviews & 
printf "done\n"

printf "\t Running Games"
sudo docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name games games &
printf "done\n"