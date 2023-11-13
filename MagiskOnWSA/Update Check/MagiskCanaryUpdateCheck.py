import os
import json
import requests
import logging
import subprocess

logging.captureWarnings(True)
env_file = os.getenv('GITHUB_ENV')

new_version_found = False

# Get current version
currentver = requests.get(f"https://raw.githubusercontent.com/WellCodeIsDelicious/WSATest/update/magiskcanary.appversion").text.replace('\n', '')
# Write for pushing later
with open('../magiskcanary.appversion', 'w') as file:
    file.write(currentver)

if not new_version_found:
    # Get latest version
    latestver = ""
    magiskcanarymsg = ""
    latestver = json.loads(requests.get(f"https://github.com/topjohnwu/magisk-files/raw/master/canary.json").content)['magisk']['version'].replace('\n', '')
    magiskcanarymsg="Update Magisk Canary Version from `v" + currentver + "` to `v" + latestver + "`"

    # Check if version is the same or not
    if currentver != latestver:
        print("New version found: " + latestver)
        new_version_found = True
        # Write appversion content
        with open('magiskcanary.appversion', 'w+') as file:
            file.seek(0)
            file.truncate()
            file.write(latestver)
        # Write Github Environment
        with open(env_file, "a") as wr:
            wr.write(f"MAGISK_CANARY_MSG={magiskcanarymsg}\n")
    file.close()        