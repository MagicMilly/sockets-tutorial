import socket

# socket is the end-point that receives communication

# socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# same machine, second part of tuple is the port
s.bind((socket.gethostname(), 1234))
# queue of 5
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    
