pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                dir('api/microservices'){
                    echo 'BUILD STARTED'
                    //sh 'pwd' 
                    echo 'Removing microservices network'
                    sh 'docker network rm microservices'
                    echo 'Creating docker network microservices'
                    sh 'docker network create microservices'
                    echo 'Creating microservices containers' 
                    sh 'docker build . -f games/Dockerfile -t games'
                    sh 'docker build . -f reviews/Dockerfile -t reviews'
                    sh 'docker build . -f users/Dockerfile -t users'
                    sh 'docker build . -f steam/Dockerfile -t steam'
                    sh 'docker build . -f gateway/Dockerfile -t gateway'
                    echo 'BUILD COMPLETED'

                } 
            }
        }
        stage("Test") {
          steps {
            echo 'Running Containers'
            /*
            sh '''
              docker run -p 127.0.0.1:50052:50052/tcp --network microservices --name users users &
              docker run -p 127.0.0.1:50053:50053/tcp --network microservices --name reviews reviews &
              docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name games games &
              docker run -p 127.0.0.1:50050:50050/tcp --network microservices --name steam steam &
              docker run -p 127.0.0.1:5000:5000/tcp --network microservices --name gateway gateway &
              pytest
            '''
            */
           sh 'pytest'
          }
        }
    }
}
