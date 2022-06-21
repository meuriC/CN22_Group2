pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')
    }
    stages {
        stage('Build') {
            steps {
                dir('api/microservices'){
                    echo 'BUILD STARTED'
                    //sh 'pwd' 
                    echo 'Removing microservices network'
                    sh 'docker network rm microservices'
                    echo 'Creating docker network microservices'
                    sh 'docker network create microservices'
                    echo 'Creating microservices containers' 
                    sh '''
                        docker build . -f games/Dockerfile -t games
                        docker build . -f reviews/Dockerfile -t reviews
                        docker build . -f users/Dockerfile -t users
                        docker build . -f steam/Dockerfile -t steam
                        docker build . -f gateway/Dockerfile -t gateway
                    '''
                    echo 'BUILD COMPLETED'

                } 
            }
        }
        stage("Test") {
           agent {
                docker {
                    image 'qnib/pytest'
                }
          }
          steps {
            echo 'Running Containers'
            sh '''
              docker run -p 127.0.0.1:50052:50052/tcp --network microservices --name users users &
              docker run -p 127.0.0.1:50053:50053/tcp --network microservices --name reviews reviews &
              docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name games games &
              docker run -p 127.0.0.1:50050:50050/tcp --network microservices --name steam steam &
              docker run -p 127.0.0.1:5000:5000/tcp --network microservices --name gateway gateway &
              pytest --cov=.
            '''
           //sh 'pytest --cov=.'
          }
        }
        stage("Delivery") {
            steps {
                echo 'Pushing images to Docker Hub'
                sh '''
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker tag steam:latest cn20222/steam-microservice:1.0
                    docker push cn20222/steam-microservice:1.0
                    docker tag games:latest cn20222/games-microservice:1.0
                    docker push cn20222/games-microservice:1.0
                    docker tag users:latest cn20222/users-microservice:1.0
                    docker push cn20222/users-microservice:1.0
                    docker tag reviews:latest cn20222/reviews-microservice:1.0
                    docker push cn20222/reviews-microservice:1.0
                    docker tag gateway:latest cn20222/gateway-microservice:1.0
                    docker push cn20222/gateway-microservice:1.0
                '''
          }
        }
    }
    post {
        always {
        sh 'docker logout'
        }
   }
}
