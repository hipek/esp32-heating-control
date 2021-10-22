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


class Main:
    def __init__(self):
        self.net_dev = NetworkDevice(Config["wifi"]["name"], Config["wifi"]["password"])
        self.mqtt_client = MQTTClient("heating_control", Config["mqtt"]["server"])
        self.exit_loop = False

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
        while not self.exit_loop:
            await asyncio.sleep(0.2)

    # async def publish_sensor(self):
    #     i = 0
    #     while True:
    #         self.mqtt_client.publish(
    #             topic="heating_control/temp",
    #             msg=json.dumps([i, await self.sensor.read(0)]),
    #         )
    #         i += 1
    #         await asyncio.sleep(10)


if __name__ == "__main__":
    main = Main()
    main.setup()
    main.start()
