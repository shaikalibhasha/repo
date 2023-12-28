pipeline {
    agent any

    stages {
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

        stage('Test') {
            steps {
                // Run tests (replace with your test commands)
                sh 'echo "Running tests..."'
		sh 'chmod +x arshan.sh' // Grant execute permissions
                sh './arshan.sh' // Replace with your actual test script
            }
        }
    }

    post {
        success {
            // Actions to be performed when the pipeline succeeds
            echo 'Build and Test succeeded!'
        }
        failure {
            // Actions to be performed when the pipeline fails
            echo 'Build or Test failed. Please check the logs for details.'
        }
    }
}


