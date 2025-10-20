pipeline {
  agent any
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // store as username/password
    IMAGE = "your-dockerhub-username/devops-pipeline-demo"
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build & Test') {
      steps {
        sh 'python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt'
        sh 'pytest -q'
      }
    }
    stage('Docker Build') {
      steps {
        script {
          IMAGE_TAG = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
          sh "docker build -t ${IMAGE}:${IMAGE_TAG} -t ${IMAGE}:latest ."
        }
      }
    }
    stage('Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
          sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
          sh "docker push ${IMAGE}:${IMAGE_TAG}"
          sh "docker push ${IMAGE}:latest"
        }
      }
    }
    stage('Deploy (example)') {
      steps {
        echo "Deploy step — implement according to your infra (ssh, k8s, helm, etc.)"
      }
    }
  }
}
