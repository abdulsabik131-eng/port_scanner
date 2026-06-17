import socket

def get_service_name(port):
    """Finds the standard service name for a given port."""
    try:
        # Built-in socket function to get service name (e.g., 80 -> http, 22 -> ssh)
        return socket.getservbyport(port, "tcp").upper()
    except:
        return "UNKNOWN SERVICE"