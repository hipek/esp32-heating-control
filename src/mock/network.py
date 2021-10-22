class WLAN:
    def __init__(self, *args):
        self.args = args

    def active(self, flag):
        self.flag = flag

    def connect(self, name, password):
        self.connected = True

    def isconnected(self):
        return self.connected

    def ifconfig(self):
        return ("192.168.1.1", "255.255.0.0", "1")


class STA_IF:
    pass
