#!/usr/bin/env python

import subprocess
import os
import sys


cmd = "ampy"
src = "src"

def system(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    return result.stdout

if len(sys.argv) > 1:
    device_files = [sys.argv[1]]
else:
    device_files = system([cmd, "ls"]).strip().split("\n")

for device_file in device_files:
    if ".py" in device_file:
        print(f"checking remote file: {device_file}")
        remote_file = system([cmd, "get", device_file]).strip()
        local_filename = os.path.join(src, *device_file.split("/"))
        f = open(local_filename)
        local_file = f.read().strip()
        f.close()
        if remote_file != local_file:
            print(f"Uploading new file: {device_file} from {local_filename}")
            system([cmd, "put", local_filename ])
