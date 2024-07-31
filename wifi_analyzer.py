import subprocess

def wifi_analyzer():
    result = subprocess.run(['nmcli', 'dev', 'wifi'], stdout=subprocess.PIPE)
    print(result.stdout.decode())