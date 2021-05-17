pipeline {
    agent any

    triggers {
        pollSCM('*/3 * * * *')
    }

    environment {
        SECRET_KEY = credentials('dorandoranSecretKey')
        DATABASE_URL = credentials('dorandoranDatabaseUrl')
        JWT_SECRET_KEY = credentials('dorandoranJwtSecretKey')
        DJANGO_SETTINGS_MODULE = credentials('dorandoranDjangoSettingsModule')
        JWT_ALGORITHM = credentials('dorandoranJwtAlgorithm')
    }

    stages {
        stage('Environ variable') {
            agent any

            steps {
                export SECRET_KEY="${env.SECRET_KEY}" DATABASE_URL="${env.DATABASE_URL}" JWT_SECRET_KEY="${env.JWT_SECRET_KEY}" JWT_ALGORITHM="${env.JWT_ALGORITHM}" DJANGO_SETTINGS_MODULE="${env.DJANGO_SETTINGS_MODULE}"
            }
        }

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
                sudo docker build . -t dorandoran-server
                """
            }
        }
        
        stage('Deploy') {
            agent any

            steps {
                echo 'Deploy Backend'

                sh '''
                sudo docker run -p 81:8000 -d dorandoran-server
                '''
            }

            post {
                failure {
                    echo 'I failed'
                }
            }
        }
    }
}