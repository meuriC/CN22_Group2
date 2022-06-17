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
                sh 'bash scripts/build_dockers.sh'
                
            }
        }
    }
}
