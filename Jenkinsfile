pipeline {
    agent any

    stages {

        stage('Setup Python') {
            steps {
                sh '''
                    echo "building"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "testing"
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    echo "deploying"
                '''
            }
        }
    }
}
