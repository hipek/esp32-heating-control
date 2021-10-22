from config import Config

def test_config_wifi():
    assert Config["wifi"]["name"]
    assert Config["wifi"]["password"]

def test_config_webrepl():
    assert Config["webrepl"]["password"]

def test_mqtt_config():
    assert Config["mqtt"]["client_id"]
    assert Config["mqtt"]["server"]
    assert Config["mqtt"]["topic_prefix"]
