pipeline {
    agent any

    environment {
        IMAGE = "sampathsanjay/project1-app"
        PYTHONUNBUFFERED = "1"
    }

    stages {

        stage('Build & Test') {
            steps {
                sh '''
                    # Remove old virtual environment
                    rm -rf .venv

                    # Create and activate virtual environment
                    python3 -m venv .venv
                    . .venv/bin/activate

                    # Upgrade pip
                    python3 -m pip install --upgrade pip==24.1

                    # Install dependencies
                    python3 -m pip install -r requirements.txt

                    # Run tests
                    python3 -m pytest -q --exitfirst tests/test_app.py
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                        # Use sudo because Jenkins user may not have Docker permission
                        echo $PASSWORD | sudo docker login -u $USERNAME --password-stdin
                        sudo docker push ${IMAGE}:latest
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







