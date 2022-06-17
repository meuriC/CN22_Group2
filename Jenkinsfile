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
                sh 'sudo scripts/build_dockers.sh'
                
            }
        }
    }
}
