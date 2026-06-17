import socket
import sys

def get_inputs():
    """Gets target and ports from user via simple terminal inputs."""
    target = input("Enter Target IP or Domain (e.g: 192.168.1.1 or google.com): ")
    port_range = input("Enter Port Range (e.g: 20-80): ")
    return target, port_range

def validate_target(target):
    """Converts domain to IP if needed, and checks if connection is possible."""
    try:
        # If user typed a domain name (like google.com), this converts it to an IP.
        # If it's already an IP, it just returns it.
        target_ip = socket.gethostbyname(target)
        return target_ip
    except socket.gaierror:
        print("[-] Error: Invalid IP address or Domain name.")
        sys.exit()

def parse_ports(port_range):
    """Splits '20-80' into a list of numbers from 20 to 80."""
    
    try:
        # Split the string by the hyphen '-'
        start, end = port_range.split("-")
        # Convert strings to integers and create a list
        return list(range(int(start),int(end)+1))
    except ValueError:
        print("** error : use format 'start-end' (e.g:20-80))")
        sys.exit()