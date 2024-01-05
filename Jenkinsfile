pipeline {
    agent any

    stages {
        stage('Checkout and Build') {
            parallel {
                stage('Checkout') {
                    steps {
                        // Checkout the source code from your Git repository
                        checkout scm
                    }
                }
                stage('Build') {
                    steps {
                        // Build your project (replace with your build commands)
                        sh 'echo "Building..."'
                        sh 'touch sample.txt' // Replace with your actual build script
                    }
                }
            }
        }

        stage('Test') {
            parallel {
                stage('Test 1') {
                    steps {
                        // Run tests (replace with your test commands)
                        sh 'echo "Running tests 1..."'
                        sh 'chmod +x arshan.sh' // Grant execute permissions
                        sh './arshan.sh' // Replace with your actual test script
                    }
                }
                stage('Test 2') {
                    steps {
                        // Run additional tests (replace with your test commands)
                        sh 'echo "Running tests 2..."'
                        // Add more test steps as needed
                    }
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t your-docker-image-name .'

                    // Push Docker image to a registry (replace with your registry details)
                    sh 'docker push your-docker-image-name'
                }
            }
        }
    }

    post {
        success {
            // Actions to be performed when the pipeline succeeds
            echo 'Build, Test, and Docker image build/push succeeded!'
        }
        failure {
            // Actions to be performed when the pipeline fails
            echo 'Build, Test, or Docker image build/push failed. Please check the logs for details.'
        }
    }
}







