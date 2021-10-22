import random


class DS18X20:
    def __init__(self, *args, **kwargs):
        self.roms = [1]

    def scan(self):
        return self.roms

    def convert_temp(self):
        pass

    def read_temp(self, index):
        return round(random.random() * 100 % 25, 2)
