pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/employee-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-app:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop employee-container || true
                docker rm employee-container || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker run -d \
                --name employee-container \
                -p 5000:5000 \
                employee-app:latest
                '''
            }
        }

    }
}
