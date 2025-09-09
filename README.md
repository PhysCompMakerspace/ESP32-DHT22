# ESP32-DHT22

Get the Arduino IDE:
https://www.arduino.cc/en/software/

To use the ESP32 with Arduino IDE, you'll need to add ESP32 boards to the list of boards available in the IDE.


In Arduino IDE, open up prefercnes: File -> Preferences...
Add the following URL to the "Additional boards manager URLs:"

https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json


ESP32 Driver:
Go to: https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers
Download the “CP210x Windows Driver” or “SiLabsUSBDriverDisk.dmg” for MacOS
Unzip and install the driver


Install the libraries below:
* Adafruit Unified Sensor
* Adafruit DHT sensor Library


