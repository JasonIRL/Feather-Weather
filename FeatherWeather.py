import time
import network
import urequests
import machine
import ht16k33_seg  # This library is available on Adafruit's GitHub

# Display #
# I am using an Adafruit 14-segment Feather Wing.
# The address can be modified if using more than one Feather Wing in your
# project.

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
display = ht16k33_seg.Seg14x4(i2c, address=0x70)
display.fill(0)
display.show()

# WiFi Setup #
# Enter your Wifi Credentials below

SSID = "WiFiName"
PASS = "WiFiPassword"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(SSID, PASS)
time.sleep(3)

# DarkSky Section #
# You will need and API key, as well as the lattitude and longitude of
# the location you want to monitor. Register for an API key at
# https://darksky.net/dev/register

APIKEY = "DarkSky.net API KEY"
LAT = "XX.XXXX"
LNG = "XX.XXXX"
EXCLUSIONS = "?exclude=minutely,hourly,daily,alerts,flags"

while True:
    WEATHER = urequests.get("https://api.darksky.net/forecast/%s/%s,%s%s"
                            % (APIKEY, LAT, LNG, EXCLUSIONS)).json()
    TEMP = int(WEATHER["currently"]["temperature"])
    display.fill(0)
    display.text(' %iF' % (TEMP))
    display.show()
    time.sleep(90)
