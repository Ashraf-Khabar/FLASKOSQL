pipeline {
    agent any

    stages {

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    source venv/bin/activate
                    python setup.py sdist bdist_wheel  # if using setuptools
                '''
            }
        }
    }
}
