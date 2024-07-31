import socket

def port_scanner(target, ports):
    print(f"Scanning {target} for open ports...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        s.close()