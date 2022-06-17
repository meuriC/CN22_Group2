pipeline {
    agent any

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'docker network create microservices'
                printf '\t Creating microservices containers' 
                sh 'docker build . -f api/microservices/games/Dockerfile -t games'
                sh 'docker build . -f api/microservices/reviews/Dockerfile -t reviews'
                sh 'docker build . -f api/microservices/users/Dockerfile -t users'
                sh 'docker build . -f api/microservices/steam/Dockerfile -t steam'
                sh 'docker build . -f api/microservices/gateway/Dockerfile -t gateway'
                printf '... done\n'
                printf '\t Building Containers with compose\n'
                sh 'docker-compose up'
                
            }
        }
    }
}
