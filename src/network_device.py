import network
import time

class NetworkDevice:
    def __init__(self, name, password):
        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(True)
        self.sta_if.connect(name, password)

    def wait_for_network(self):
        while not self.sta_if.isconnected():
            time.sleep(1)
            print("waiting for wifi")
        print("connected!")
