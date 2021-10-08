def secret(name):
    f = open(name, "r")
    val = f.read()
    f.close()
    return val.strip()


Config = {"wifi": {"name": "bbb333", "password": secret("wifi_password")}}
