pipeline {
    agent any;
    options {
        buildDiscarder logRotator( 
                    daysToKeepStr: '16', 
                    numToKeepStr: '10'
            )
    }

    stages {
        
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
                sh """
                echo "Cleaned Up Workspace For Project"
                """
            }
        }

        stage('Code Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: 'demo']], 
                    userRemoteConfigs: [[url: 'https://github.com/TestSubject8/djano-website']]
                ])
            }
        }

        stage('Move code') {
            steps {
                sh """
                mv * /home/website/demosite/
                """
            }
        }

        // stage('Restart webserver'){
        //     steps {

        //     }
        // }


        // stage('Build Deploy Code') {
        //     when {
        //         branch 'develop'
        //     }
        //     steps {
        //         sh """
        //         echo "Building Artifact"
        //         """

        //         sh """
        //         echo "Deploying Code"
        //         """
        //     }
        // }

    }   
}