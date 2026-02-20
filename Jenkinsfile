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
    stage('Acepte key ssh') {
      steps {
        sh'mkdir -p ~/.ssh'
        sh 'python3 script/main.py'
      }
    }

    stage('Configuracion inicial suse') {
      steps {
        sh 'ansible-playbook -i inventories/igeomat.yaml playbooks/initconfig.yaml -e "ansible_password=${root_passwd}"'
      }
    }
  }
}