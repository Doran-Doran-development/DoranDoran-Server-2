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
                    branch : 'develop',
                    credentialsId: 'githubTokenForJenkinshanbin8269'
            }

        }

        stage('Build Image') {
            agent any
            steps {
                echo 'Build Backend Image'

                sh '''
                sudo docker build . -t ${IMAGE_NAME}
                '''
            }
        }
        
        stage('Deploy Container') {
            agent any

            steps {
                echo 'Stop and Remove existed container'
                sh '''
                sudo docker stop ${CONTAINER_NAME} || true && sudo docker rm ${CONTAINER_NAME} || true
                '''
                
                echo 'Run new container'
                sh '''
                sudo docker run --name ${CONTAINER_NAME} -p ${EXTERNAL_PORT}:8000 -d \
                -e DATABASE_URL=${DATABASE_URL} \
                -e SECRET_KEY=${SECRET_KEY} \
                -e JWT_SECRET_KEY=${JWT_SECRET_KEY} \
                -e JWT_ALGORITHM=${JWT_ALGORITHM} \
                -e DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE} \
                -e EMAIL_HOST_USER=${EMAIL_HOST_USER} \
                -e EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD} \
                ${IMAGE_NAME}
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