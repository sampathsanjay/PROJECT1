pipeline {
  agent any
  environment {
    IMAGE = "sampathsanjay/project1-app"
  }
  stages {
    stage('Build & Test') {
      steps {
        sh '''
          python3 -m venv .venv && \
          . .venv/bin/activate && \
          python3 -m pip install --upgrade pip && \
          python3 -m pip install -r requirements.txt && \
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



