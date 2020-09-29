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
                    branches: [[name: 'flask-demo']], 
                    userRemoteConfigs: [[url: 'https://github.com/TestSubject8/portfolio-website']]
                ])
            }
        }

        stage('Move code') {
            steps {
                sh """
                rm -r /home/website/portfolio-website/*
                mv * /home/website/portfolio-website/
                """
            }
        }

        stage('Restart webserver'){
            steps {
                dir("/home/website/portfolio-website/"){
                    sh """
                    python3 -m virtualenv basic-env -p python3
                    source basic-env/bin/activate && pip install -r requirements.txt 
                    sudo systemctl restart uwsgi-app
                    sudo systemctl restart nginx
                    """
                }
	    }
        }
    }   
}
