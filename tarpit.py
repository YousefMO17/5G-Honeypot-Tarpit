import socket 
import time

#IP and port to listen on 
#Receive from any IP address and use port 2222
HOST="0.0.0.0"
PORT=2222

print(f"🍯 [HONEYPOT DEPLOYED] Fake 5G Core Router listening on port {PORT}...")
print("🕷️ Waiting for hackers to fall into the trap...\n")

#TCP , IPV4 IDENTIFIER
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#FOR RESUMING THE CONNECTION WITHOUT WAITING FOR THE TIMEOUT
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

while True:
    client_connection = None 
    
    try:
        client_connection, client_address = server_socket.accept()
        print(f"🚨 [INTRUSION DETECTED] Unauthorized connection from IP: {client_address[0]}")
        
        banner = b"WARNING: Authorized Personnel Only.\r\nConnected to Vodafone 5G Core Router (Admin Interface).\r\nPassword: "
        client_connection.sendall(banner)
        
    
        hacker_input = client_connection.recv(1024).decode('utf-8').strip()
        print(f"🕵️ [THREAT INTEL] Hacker attempted to use password: '{hacker_input}'")
        
        print(f"⏳ [TARPIT ACTIVE] Trapping IP {client_address[0]} in an infinite loop...")
        
        while True:
            client_connection.sendall(b"......")
            time.sleep(10)
            
    except Exception as e:
        print(f"💨 [HACKER DROPPED] Connection closed. ({e})")
        
    finally:
        if client_connection is not None:
            client_connection.close()