import ipaddress
import socket

class PortScanner:

    firstOptions()

    """
    Initialize port scanner.

    """
    def __init__(self, target):
        self.target = target
        self.results = []

    def scanAllPorts():
        for port in range(1, 6535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



