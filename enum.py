import socket
import argparse

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def conexão_ftp(ip):
    try:
        tcp = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
        tcp.connect(ip, 21)
