pipeline {
    agent any

    stages {
        stage('Clean and Build') {
            agent any
            environment{
                CONTAINERS = '$(docker ps -a -q)'
                IMAGES = '$(docker images -aq)'
            }
            steps {
                echo 'Clean all docker images'
                echo 'Removing microservices network'
                sh 'docker network rm microservices'
                echo 'CLEAN COMPLETE'
                sh 'docker network create microservices'
                echo '\t Creating microservices containers' 
                sh 'docker build . -f api/microservices/games/Dockerfile -t games'
                sh 'docker build . -f api/microservices/reviews/Dockerfile -t reviews'
                sh 'docker build . -f api/microservices/users/Dockerfile -t users'
                sh 'docker build . -f api/microservices/steam/Dockerfile -t steam'
                sh 'docker build . -f api/microservices/gateway/Dockerfile -t gateway'
                echo '... done\n'
                echo '\t Building Containers with compose\n'
                sh 'docker-compose up'
                
            }
        }
    }
}
