import requests
import ctypes
import datetime
import time
import os

url = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/5424x5424.jpg"       # GOES-EAST Full
# url = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/5000x3000.jpg"  # Continenetal US

script_path = os.getcwd()

def update_image():
    with requests.get(url) as req:
        with open("latest.jpg", "wb") as img:
            img.write(req.content)

    # set image as background
    ctypes.windll.user32.SystemParametersInfoW(20, 0, script_path + "\latest.jpg", 0)

    print("Updating image:", str(datetime.datetime.now()))


if __name__ == "__main__":
    # delete previous image
    if os.path.exists("latest.jpg"):
        os.remove("latest.jpg")

    while 1:
        update_image()

        # 10 min delay
        time.sleep(600)

# end file
