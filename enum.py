import socket
import argparse

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def conexão_ftp(ip):
    try:
        tcp = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
        tcp.connect(ip, 21)
        
        #enviando conexão
        print(f"{RED}Conectando ao servidor...{RESET}")
        banner = tcp.recv(1024).decode('utf-8')
        print(f"{GREEN}{banner}{RESET}")

        # aqui envia o user !!! :)
        print(f"{RED}Enviando USER...{RESET}")
        tcp.send("USER ftp\r\n".encode('utf-8'))
        user = tcp.recv(1024).decode('utf-8')
        print(f"{GREEN}{user}{RESET}")

        # enviando a senha
        print(f"{RED}Enviando PASS...{RESET}")
        tcp.send("PASS ftp\r\n".encode('utf-8'))
        pw = tcp.recv(1024).decode('utf-8')
        print(f"{GREEN}{pw}{RESET}")

        # pwd
        print(f"{RED}Enviando comando PWD...{RESET}")
        tcp.send("PWD\r\n".encode('utf-8'))
        cmd = tcp.recv(2048).decode('utf-8')
        print(f"{GREEN}{cmd}{RESET}")




