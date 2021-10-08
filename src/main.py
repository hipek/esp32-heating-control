import ntptime
import machine
import time
import json
import utime
import webrepl

from config import Config
from network_device import NetworkDevice
from sensors import Ds18b20Sensor
from mqtt import MQTTClient

net_dev = NetworkDevice(Config["wifi"]["name"], Config["wifi"]["password"])
net_dev.wait_for_network()

webrepl.start(password="test")

ntptime.settime()

sensor = Ds18b20Sensor(machine.Pin(22))

client = MQTTClient("heating_control", Config["mqtt"]["server"])
client.connect()


def loop():
    start_time = time.ticks_ms()
    interval = 60000

    while True:
        if time.ticks_ms() - start_time >= interval:
            start_time = time.ticks_ms()

            client.publish(
                topic="heating_control/temp",
                msg=json.dumps([sensor.read(0), sensor.read(1), utime.localtime()]),
            )


loop()
