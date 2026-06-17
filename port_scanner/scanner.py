import socket

def scan_ports(target_ip, port_list):
    """Loops through the ports and checks which ones are open."""
    open_ports = []
    print(f"\n[*] Scanning {target_ip}...")

    for port in port_list:
        # Create a basic TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Wait maximum 0.5 seconds for a response
        
        # connect_ex returns 0 if the port is open
        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            open_ports.append(port)
            
        sock.close() # Always close the socket!
        
    return open_ports