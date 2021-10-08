import ntptime
import machine

from config import Config
from network_device import NetworkDevice
from sensors import Ds18b20Sensor


net_dev = NetworkDevice(Config["wifi"]["name"], Config["wifi"]["password"])
net_dev.wait_for_network()

ntptime.settime()

sensor = Ds18b20Sensor(machine.Pin(4))


def loop():
    for i in range(0, 5):
        print(sensor.read())
