import socket

def network_sniffer():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = s.recvfrom(65535)
        print(f"Packet from {addr}: {raw_data}")