import socket
import threading

def handle_client(client_socket):

#function reads data from the client, checks if its "Hello"
  request = client_socket.recv(1024)
  if request.decode() == "Hello";
    response = "Hi"
else: 
  response = "Goodbye"
client_socket.send(response.encode())


client_socket.close()

def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #the server listens for incoming connections on port 9500.

    server.bind(("0.0.0.0", 9500))

if __name__ == "__main__":
  main()
