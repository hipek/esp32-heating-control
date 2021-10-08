# get the firmware

	https://micropython.org/download/#esp32
	https://micropython.org/download/esp32/
 	https://micropython.org/resources/firmware/esp32-20210902-v1.17.bin

# erase the flash while holding boot button

	esptool.py --port /dev/ttyUSB0 erase_flash

# deploy the new firmware

    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
    esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin

# deploy on mac

# testing

	https://github.com/tflander/esp32-machine-emulator

# list files

    ampy ls
