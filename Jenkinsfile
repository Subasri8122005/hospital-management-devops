pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Subasri8122005/hospital-management-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hospital-management-app:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
                    docker rm -f hospital-management-app 2>NUL || exit /B 0
                    docker run -d --name hospital-management-app -p 5000:5000 hospital-management-app:latest
                '''
            }
        }
    }
}                  
                    
