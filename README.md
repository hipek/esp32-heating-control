# Install

    pip install -r requirements.txt

# get the firmware

	https://micropython.org/download/#esp32
	https://micropython.org/download/esp32/
 	https://micropython.org/resources/firmware/esp32-20210902-v1.17.bin

# erase the flash while holding boot button

	esptool.py --port /dev/ttyUSB0 erase_flash

# deploy the new firmware

    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin

# testing

	https://github.com/tflander/esp32-machine-emulator

# list files

    ampy ls

# deploy updated python files

     ./tools/sync.py

# deploy one updated python files

     ./tools/sync.py main.py

# deploy new pyton file

    ampy put src/new_file.py
