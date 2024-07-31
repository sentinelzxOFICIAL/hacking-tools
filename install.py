import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and handle errors."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.stderr.decode())
        sys.exit(1)

def install_packages():
    """Install necessary packages."""
    print("Atualizando pacotes e repositórios...")
    run_command("pkg update -y && pkg upgrade -y")

    print("Instalando dependências básicas...")
    run_command("pkg install -y python python-pip git curl")

    print("Instalando ferramentas adicionais...")
    run_command("pkg install -y clang openssl libffi")

    print("Corrigindo possíveis problemas de instalação...")
    run_command("pip install --upgrade pip setuptools wheel")

    print("Instalando pacotes diretamente...")
    run_command("pip install termcolor")
    run_command("pip install paramiko")

    print("Instalação completa.")

def main():
    install_packages()
    print("Para utilizar as ferramentas que requerem root (Network Sniffer e Wi-Fi Analyzer), certifique-se de executar com privilégios de root.")
    print("Iniciando o script principal...")
    run_command("python main.py")

if __name__ == "__main__":
    main()