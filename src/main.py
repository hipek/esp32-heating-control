import json

import machine

try:
    import uasyncio as asyncio
except:
    import asyncio

try:
    import utime
except:
    import time as utime

try:
    from mqtt import MQTTClient
except:
    from mock.mqtt import MQTTClient

import ntptime
import webrepl

from config import Config
from network_device import NetworkDevice
from sensors import Ds18b20Sensor


class Main:
    def __init__(self):
        self.net_dev = NetworkDevice(Config["wifi"]["name"], Config["wifi"]["password"])
        self.sensor = Ds18b20Sensor(machine.Pin(25))
        self.mqtt_client = MQTTClient("heating_control", Config["mqtt"]["server"])

    def setup(self):
        self.net_dev.wait_for_network()
        ntptime.settime()
        self.mqtt_client.connect()
        webrepl.start(password=Config["webrepl"]["password"])

        try:
            import uftpd
        except:
            print("uftpd can't be imported")

    def reset(self):
        machine.reset()

    def start(self):
        asyncio.run(self.loop())

    async def loop(self):
        asyncio.create_task(self.publish_sensor())
        asyncio.create_task(self.receive_command())
        while True:
            await asyncio.sleep(1)

    async def publish_sensor(self):
        i = 0
        while True:
            self.mqtt_client.publish(
                topic="heating_control/temp",
                msg=json.dumps([i, await self.sensor.read(0)]),
            )
            i += 1
            await asyncio.sleep(10)

    async def receive_command(self):
        i = 0
        while True:
            t = utime.localtime()
            self.mqtt_client.publish(
                topic="heating_control/watchdog",
                msg=json.dumps([i, f"{t[0]}-{t[1]}-{t[2]}T{t[3]}:{t[4]}:{t[5]}Z"]),
            )
            i += 1
            await asyncio.sleep(60)


main = Main()
main.setup()
main.start()
