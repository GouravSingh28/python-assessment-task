pipeline {
    agent any

    environment {
        REGISTRY   = "python01registry.azurecr.io"
        IMAGE_NAME = "pythonsample"
        CONTAINERNAME = "python01registry.azurecr.io/pythonsample"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker --version
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Login to Registry') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-registry-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login python01registry.azurecr.io -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${CONTAINERNAME}:${IMAGE_TAG}
                docker push ${CONTAINERNAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo "Docker image pushed successfully "
        }
        failure {
            echo "Pipeline failed "
        }
        always {
            sh 'docker logout || true'
        }
    }
}
