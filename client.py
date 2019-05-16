import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# how much data (bytes) do you want to receive at a time - buffer size
# while True allows the server to handle data larger than the limit you set, just will be
# sent in chunks based on limit
while True:
    msg = s.recv(8)
    # send and receive bytes, so need to be decoded
    print(msg.decode("utf-8"))