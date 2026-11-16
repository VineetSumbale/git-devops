pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh '''
                    echo team
                    echo morning class
                '''

                retry(3) {
                    sh 'echo trying....'
                }

                timeout(time: 15, unit: 'SECONDS') {
                    sh 'sleep 30'
                }
            }
        }
    }
}
