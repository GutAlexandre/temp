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
                // Démarrer l'application Flask
                sh 'python3 jeDanseLeMain.py &'
            }
        }
    }
    
}
