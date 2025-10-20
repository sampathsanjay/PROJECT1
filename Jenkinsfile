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

          # Activate venv and install dependencies
          . .venv/bin/activate
          python3 -m pip install --upgrade pip==24.1
          python3 -m pip install -r requirements.txt

          # Run tests
          python3 -m pytest -q
        '''
      }
    }

    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh '''
            echo $PASSWORD | docker login -u $USERNAME --password-stdin
            docker push ${IMAGE}:latest
          '''
        }
      }
    }
  }
}




