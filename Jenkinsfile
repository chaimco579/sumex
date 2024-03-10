pipeline {
    agent any
    stages {
        stage('git clone') {
            steps {
                deleteDir()
                sh 'echo cloning project...'
                sh 'git clone https://github.com/chaimco579/sumex.git'
            }
        }

        stage('docker compose build') {
            steps {
                dir('sumex') {
                        sh 'docker-compose up -d'
                    }
                }
         } 
        stage('docker ps') {
          steps{
            sh 'docker ps'
          }
        }
    }
}
