pipeline {
    agent any
    stages {
	stage('verison') {
	     steps {
	         sh 'python3 --version'
	     }
	}
          stage('Run Python Script') { 
                steps { 
		sh 'python3 Robot.py' 
		} 
	      } 
	}
}
