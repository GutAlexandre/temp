pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Construire l'image Docker
                    docker.build('flask-app', '-f Dockerfile .')
                }
            }
        }
        
        stage('Run Docker Container') {
            steps {
                script {
                    // Exécuter le conteneur Docker à partir de l'image précédemment construite
                    docker.image('flask-app').run('-d -p 5000:5000')
                }
            }
        }
    }
}
