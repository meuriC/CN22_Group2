pipeline {
    agent any

    stages {
        stage('Clean and Build') {
            agent any
            steps {
                echo 'Clean all docker images'
                sh "docker stop $(docker ps -a -q)"
                sh "docker rm $(docker ps -a -q)"
                sh "docker rmi -f $(docker images -aq)"
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
