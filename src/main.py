import json

import machine
import uasyncio
import utime

import ntptime
import webrepl
from config import Config
from mqtt import MQTTClient
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
        webrepl.start(password="test")

        import uftpd

    def reset(self):
        machine.reset()

    async def loop(self):
        uasyncio.create_task(self.publish_sensor())
        uasyncio.create_task(self.receive_command())
        while True:
            await uasyncio.sleep(1)

    async def publish_sensor(self):
        i = 0
        while True:
            self.mqtt_client.publish(
                topic="heating_control/temp",
                msg=json.dumps([i, await self.sensor.read(0)]),
            )
            i += 1
            await uasyncio.sleep(10)

    async def receive_command(self):
        i = 0
        while True:
            self.mqtt_client.publish(
                topic="heating_control/watchdog",
                msg=json.dumps([i]),
            )
            i += 1
            await uasyncio.sleep(60)


main = Main()
main.setup()

uasyncio.run(main.loop())
