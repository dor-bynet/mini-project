pipeline {
    agent any
    options {
        ansiColor('xterm')
    }
    stages {
        stage('Clone GitHub repo') {
            steps {
                git branch: 'main', url: 'https://github.com/dor-bynet/mini-project.git'
                sh(script: "python3 ./newton_binomial.py")
            }
        }
    }
}
