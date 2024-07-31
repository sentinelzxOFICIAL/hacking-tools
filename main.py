import os
import sys
from termcolor import colored
from port_scanner import port_scanner
from network_sniffer import network_sniffer
from password_cracker import password_cracker
from hash_cracker import hash_cracker
from wifi_analyzer import wifi_analyzer
from ssh_bruteforce import ssh_bruteforce

def print_menu():
    print(colored("=== Ethical Hacking Tools ===", 'cyan'))
    print(colored("1. Port Scanner", 'green'))
    print(colored("2. Network Sniffer [root]", 'red'))
    print(colored("3. Password Cracker", 'green'))
    print(colored("4. Hash Cracker", 'green'))
    print(colored("5. Wi-Fi Analyzer [root]", 'red'))
    print(colored("6. SSH Bruteforce", 'green'))
    print(colored("0. Exit", 'yellow'))

def main():
    while True:
        print_menu()
        choice = input(colored("Choose an option: ", 'blue'))
        if choice == '1':
            target = input("Enter target IP: ")
            ports = range(1, 1024)
            port_scanner(target, ports)
        elif choice == '2':
            if os.geteuid() != 0:
                print(colored("Network Sniffer requires root privileges.", 'red'))
            else:
                network_sniffer()
        elif choice == '3':
            hash_to_crack = input("Enter the hash to crack: ")
            hash_function = 'md5'  # or 'sha1'
            charset = "abcdefghijklmnopqrstuvwxyz"
            max_length = 5
            password_cracker(hash_to_crack, hash_function, charset, max_length)
        elif choice == '4':
            hash_to_crack = input("Enter the hash to crack: ")
            hash_function = 'md5'  # or 'sha1'
            wordlist = 'wordlist.txt'
            hash_cracker(hash_to_crack, hash_function, wordlist)
        elif choice == '5':
            if os.geteuid() != 0:
                print(colored("Wi-Fi Analyzer requires root privileges.", 'red'))
            else:
                wifi_analyzer()
        elif choice == '6':
            target = input("Enter target IP: ")
            username = input("Enter SSH username: ")
            password_list = ['123456', 'password', 'admin']
            ssh_bruteforce(target, username, password_list)
        elif choice == '0':
            print(colored("Exiting...", 'yellow'))
            sys.exit()
        else:
            print(colored("Invalid choice. Please try again.", 'red'))

if __name__ == "__main__":
    main()