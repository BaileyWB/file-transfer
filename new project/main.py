import socket

def send_file(file_path, receiver_ip, receiver_port):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the receiver
        sock.connect((receiver_ip, receiver_port))
        
        # Open the file to be sent
        with open(file_path, 'rb') as file:
            # Read file contents
            file_data = file.read()
            
            # Send file size
            file_size = len(file_data)
            sock.sendall(file_size.to_bytes(4, byteorder='big'))
            
            # Send file data
            sock.sendall(file_data)
            
            print("File sent successfully!")
    
    finally:
        # Close the socket
        sock.close()

def receive_file(save_path, port):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to the port
        sock.bind(('', port))
        
        # Listen for incoming connections
        sock.listen(1)
        print("Waiting for connection...")
        
        # Accept a connection
        conn, addr = sock.accept()
        print("Connected to", addr)
        
        # Receive file size
        file_size_bytes = conn.recv(4)
        file_size = int.from_bytes(file_size_bytes, byteorder='big')
        
        # Receive file data
        file_data = conn.recv(file_size)
        
        # Save the received file
        with open(save_path, 'wb') as file:
            file.write(file_data)
        
        print("File received successfully and saved as", save_path)
    
    finally:
        # Close the connection and socket
        conn.close()
        sock.close()

if __name__ == "__main__":
    choice = input("Do you want to send or receive a file? (send/receive): ").lower()
    
    if choice == "send":
        file_path = input("Enter the path of the file to send: ")
        receiver_ip = input("Enter the IP address of the receiver: ")
        receiver_port = int(input("Enter the port number of the receiver: "))
        send_file(file_path, receiver_ip, receiver_port)
    elif choice == "receive":
        save_path = input("Enter the path to save the received file: ")
        port = int(input("Enter the port number to listen on: "))
        receive_file(save_path, port)
    else:
        print("Invalid choice.")
