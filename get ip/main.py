import socket

def get_ip_address():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Connect to a remote server (doesn't need to be reachable)
        sock.connect(("8.8.8.8", 80))
        
        # Get the local IP address
        ip_address = sock.getsockname()[0]
        return ip_address
        
    finally:
        # Close the socket
        sock.close()

if __name__ == "__main__":
    ip_address = get_ip_address()
    print("Your IP address is:", ip_address)
