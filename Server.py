import socket
import threading

def handle_client(client_socket):

#function reads data from the client, checks if its "Hello"
  request = client_socket.recv(1024)
  if request.decode() == "Hello";
    response = "Hi"
else: 
  response = "Goodbye"
