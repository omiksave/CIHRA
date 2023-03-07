import socket

class Client:
    def __init__(self, HOST, PORT):
        self.host = HOST
        self.port = PORT
        print("Attempting to connect......\n")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.socket:
                self.socket.connect((self.host, self.port))
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 28)
                print("Success!\n")
        except:
            print("Failed to connect!\n")
    def update(self):
        self.data = self.socket.recv(28)
        print('Received', repr(self.data))


c = Client("127.0.0.1", 5001)
c.update()
