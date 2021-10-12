class WLAN:
    def __init__(self, mode):
        self.mode = mode

    def active(self, flag):
        self.flag = flag

    def connect(self, name, passowrd):
        pass

    def isconnected(self):
        return True

    def ifconfig(self):
        return ("192.168.1.30", "255.255.255.0", "192.168.1.1")


class STA_IF:
    pass
