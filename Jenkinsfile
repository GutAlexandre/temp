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
                script {
                    // Lancer l'application Flask en arrière-plan
                    def proc = sh(script: 'nohup python3 jeDanseLeMain.py > output.log 2>&1 &', returnStdout: true)
                    // Récupérer l'adresse IP du serveur Flask à partir de la sortie du processus
                    def ip = sh(script: 'ifconfig')
                    echo "Serveur Flask lancé à l'adresse : ${ip}"
                }
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
