import socket

# AF_INET is ipv4; SOCK_STREAM is TCP, SOCK_DGRAM is UDP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#allow socket to be reused
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 9999

def do_server():
  tcp.bind((host, port))
  tcp.listen(5) # listen to at most 5 connections
  print("Server started. Listening on port", port)
  while True:
      csocket, addr = tcp.accept()
      print(f"Client connected: {addr}")
      # send a message to the client
      msg = "Thanks for connecting!".encode('ascii')
      csocket.send(msg)
      # close the connection
      csocket.close()


def do_client():
    tcp.connect((host, port))
    msg = tcp.recv(1024) # receive at most 1024 bytes
    tcp.close()
    print(f"Received server message: {msg.decode('ascii')}")

choice = input("Do you want to run as a server or client?: ")
if choice in "client":
    do_client()
else:
    do_server()