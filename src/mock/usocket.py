import socket as psocket


class Socket:
    def __init__(self):
        self.socket = psocket.socket()

    def write(self, *args):
        return self.socket.send(*args)

    def connect(self, *args):
        return self.socket.connect(*args)


def getaddrinfo(*args, **kwargs):
    return psocket.getaddrinfo(*args, **kwargs)


def socket():
    return Socket()
