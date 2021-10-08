import ntptime

from config import Config
from network_device import NetworkDevice


def setup():
    net_dev = NetworkDevice(Config["wifi"]["name"], Config["wifi"]["password"])
    net_dev.wait_for_network()

    ntptime.settime()


setup()
