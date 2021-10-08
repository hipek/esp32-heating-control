import onewire, ds18x20, time


class Ds18b20Sensor:
    def __init__(self, ds_pin):
        self.ds_pin = ds_pin
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(self.ds_pin))
        self.roms = self.ds_sensor.scan()

    def read(self, index=0):
        self.ds_sensor.convert_temp()
        time.sleep_ms(750)
        return self.ds_sensor.read_temp(self.roms[index])
