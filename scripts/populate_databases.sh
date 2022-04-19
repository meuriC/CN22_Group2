 #!/bin/sh

########################################################

## Shell Script to Populate databases

########################################################

printf "Populating Databases\n"
printf "\t Populating Games"
# { python3 "./api/databases/games/PopulateGames.py" } &> /dev/null
printf "done\n"

printf "\t Populating Reviews"
# { python3 "./api/databases/reviews/PopulateReviews.py"
#  python3 "./api/databases/reviews/PopulateReviews2.py" } &> /dev/null
printf "done\n"

printf "\t Populating Users"
# { python3 "./api/databases/reviews/PopulateUsers.py" &> /dev/null
printf "done\n" 
