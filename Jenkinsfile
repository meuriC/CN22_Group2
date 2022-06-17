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
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r api/microservices/games/requirements.txt'
                
            }
        }
    }
}
