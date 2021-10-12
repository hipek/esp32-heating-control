import os


def secret(name):
    if hasattr(os, "environ") and os.environ.get("TEST") == "true":
        f = open("secrets/" + name, "r")
    else:
        f = open(name, "r")
    val = f.read()
    f.close()
    return val.strip()


Config = {
    "wifi": {"name": "bbb333", "password": secret("wifi_password")},
    "mqtt": {"server": secret("mqtt_server")},
}
