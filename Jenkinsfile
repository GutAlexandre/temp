pipeline {
    agent any
    
    stages {
        stage('Installation des dépendances') {
            steps {
                sh 'python3 -m pip install flask-socketio flask python-can --break-system-packages'
            }
        }
        
        stage('Lancement de l\'application') {
            steps {
                // Démarrer l'application Flask en arrière-plan avec nohup
                sh 'nohup python3 jeDanseLeMain.py > output.log 2>&1 &'
            }
        }
    }
    
    post {
        always {
            // Archiver le dossier contenant l'application Flask pour afficher sur l'interface web
            archiveArtifacts 'templates/**/*,static/**/*'
            
            // Publier le rapport HTML pour afficher sur l'interface web
            publishHTML target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'templates',
                reportFiles: 'index.html',
                reportName: 'Flask Application'
            ]
        }
    }
}
