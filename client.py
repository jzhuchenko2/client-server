
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9500))  # Connect to the server on port 9500

    message = "Hello"

    #the client connects to the server, sends "Hello," and receives the server's response, printing it to the console
    client.send(message.encode())

    response = client.recv(1024)
    print(f"Server response: {response.decode()}")

    client.close()

if __name__ == "__main__":
    main()


"""Answers to B.
1. I spent 1 and a half cleaning up the main function since they were the most time I spent on during this assignment.
2. Having the server send a string "Hello" for the client by using the method send (b"Hello").
3. Deciding the library was the first confusing part; however, when I found socket and threading, coding the infinite loop was the most frustrating part of this experience. To have the server wait for the incoming client connection was confusing especially since I couldn't tell the different from using the accept() method that calls the server object. 
4. I would love to learn more about the TP Monitors since they are middleware of client requests and different applications.  
5. A brief description about the specific client and server (handle_client) functions. Unless, theres no correct way to building this application. 
"""