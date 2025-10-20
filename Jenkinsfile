pipeline {
  agent any
  environment {
    DOCKERHUB_CREDENTIALS = credentials('docker-creds')
    IMAGE = "sampathsanjay/project1-app"
  }
  stages {
    stage('Build & Test') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt
          pytest -q
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

