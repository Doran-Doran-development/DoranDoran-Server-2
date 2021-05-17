pipeline {
    agent any

    triggers {
        pollSCM('*/3 * * * *')
    }

    stages {
        stage('Prepare') {
            agent any

            steps {
                echo 'Clonning Repository'

                git url: 'https://github.com/Doran-Doran-development/DoranDoran-Server-2.git',
                    branch : 'release/1.0',
                    credentialsId: 'githubTokenForJenkinshanbin8269'
            }

        }

        stage('Build Image') {
            agent any
            steps {
                echo "Build Backend Image"

                sh """
                docker build . -t dorandoran-server
                """
            }
        }
        
        stage('Deploy') {
            agent any

            steps {
                echo 'Deploy Backend'

                sh '''
                docker run -p 81:8000 -d dorandoran-server
                '''
            }
        }
    }
}