pipeline {
    agent{
        node{
            label 'agent001'
        }
    }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Configuracion inicial suse') {
      steps {
        sh 'ansible-playbook -i inventories/igeomat.yaml playbooks/initconfig.yaml'
      }
    }
  }
}