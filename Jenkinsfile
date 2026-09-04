pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Subasri8122005/hospital-management-devops.git'
            }
        }

        stage('Verify Kubernetes Access') {
            steps {
                bat 'kubectl --kubeconfig "C:\\ProgramData\\Jenkins\\.kube\\config" config current-context'
                bat 'kubectl --kubeconfig "C:\\ProgramData\\Jenkins\\.kube\\config" get nodes'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hospital-management-app:latest .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl --kubeconfig "C:\\ProgramData\\Jenkins\\.kube\\config" apply -f k8s/'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl --kubeconfig "C:\\ProgramData\\Jenkins\\.kube\\config" get pods'
                bat 'kubectl --kubeconfig "C:\\ProgramData\\Jenkins\\.kube\\config" get service'
            }
        }
    }
}
