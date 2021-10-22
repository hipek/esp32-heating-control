from paho.mqtt.client import Client


class MQTTClient:
    def __init__(self, client_id, server):
        self.client_id = client_id
        self.server = server
        self.mqtt_client = Client()
        self.mqtt_client.connect(server)

    def connect(self):
        self.mqtt_client.connect(self.server)
        self.mqtt_client.loop_start()

    def publish(self, topic, msg, **kwargs):
        self.mqtt_client.publish(topic, msg)
