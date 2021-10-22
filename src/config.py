def secret(name):
    f = open("secrets/" + name, "r")
    val = f.read()
    f.close()
    return val.strip()


Config = {
    "wifi": {
        "name": "bbb333",
        "password": secret("wifi_password"),
    },
    "mqtt": {
        "client_id": "micropython",
        "server": secret("mqtt_server"),
        "topic_prefix": "micropython/test",
    },
    "webrepl": {
        "password": secret("webrepl_password"),
    },
    "sensors": [],
    "switches": [],
}
