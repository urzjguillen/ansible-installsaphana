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
        sh 'echo $root_passwd'
        sh 'ansible-playbook -i inventories/igeomat.yaml playbooks/initconfig.yaml -e "root_passwd=${root_passwd}"'
      }
    }
  }
}