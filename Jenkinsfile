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
                sh 'docker build -t hospital-management-app:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker rm -f hospital-management-app 2>/dev/null || true
                    docker run -d \
                        --name hospital-management-app \
                        -p 5000:5000 \
                        hospital-management-app:latest
                '''
            }
        }
    }
}
