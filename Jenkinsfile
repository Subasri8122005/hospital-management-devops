pipeline {
    agent any

    environment {
    KUBECONFIG = "${env.USERPROFILE}\\.kube\\config"
}


    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Subasri8122005/hospital-management-devops.git'
            }
        }

        stage('Verify Kubernetes Access') {
            steps {
                bat 'kubectl config current-context'
                bat 'kubectl get nodes'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hospital-management-app:latest .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get service'
            }
        }
    }
}
