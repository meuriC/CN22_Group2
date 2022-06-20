pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            environment{
                CONTAINERS = '$(docker ps -a -q)'
                IMAGES = '$(docker images -aq)'
            }
            steps {
                sh 'cd api/microservices'
                sh 'pwd' 
                echo 'Removing microservices network'
                sh 'docker network rm microservices'
                echo 'BUILD STARTED'
                echo 'Creating docker network microservices'
                sh 'docker network create microservices'
                echo 'Creating microservices containers' 
                sh 'docker build . -f games/Dockerfile -t games'
                sh 'docker build . -f reviews/Dockerfile -t reviews'
                sh 'docker build . -f users/Dockerfile -t users'
                sh 'docker build . -f steam/Dockerfile -t steam'
                sh 'docker build . -f gateway/Dockerfile -t gateway'
                echo 'Building Containers with compose'
                sh 'docker-compose up'
                echo 'BUILD COMPLETED'
                
            }
        }
    }
}
