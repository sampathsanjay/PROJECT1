pipeline {
    agent any
    environment {
        IMAGE = "sampathsanjay/project1-app"
    }
    stages {

        stage('Build & Test') {
            steps {
                sh '''
                    # Remove old virtual environment
                    rm -rf .venv

                    # Create new virtual environment
                    python3 -m venv .venv

                    # Activate virtual environment
                    . .venv/bin/activate

                    # Upgrade pip
                    python3 -m pip install --upgrade pip==24.1

                    # Install dependencies
                    python3 -m pip install -r requirements.txt

                    # Run tests in the tests/ folder
                    python3 -m pytest -q tests/test_app.py
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push ${IMAGE}:latest
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline succeeded: Tests passed and Docker image pushed.'
        }
        failure {
            echo 'Pipeline failed. Check logs for errors.'
        }
    }
}






