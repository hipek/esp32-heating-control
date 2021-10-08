import ntptime
import machine
import time
import json

from config import Config
from network_device import NetworkDevice
from sensors import Ds18b20Sensor


net_dev = NetworkDevice(Config["wifi"]["name"], Config["wifi"]["password"])
net_dev.wait_for_network()

ntptime.settime()

sensor = Ds18b20Sensor(machine.Pin(22))

client = MQTTClient("heating_control", Config["mqtt"]["server"])
client.connect()


def loop():
    for i in range(0, 5):
        client.publish(topic="heating_control/temp", msg=json.dumps([sensor.read(0), sensor.read(1)]))
        time.sleep(1)

loop()
