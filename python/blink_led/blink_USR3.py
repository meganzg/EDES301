#!/usr/bin/env python3
"""
--------------------------------------------------------------------------
Blink USR3 LED at 5Hz
--------------------------------------------------------------------------
License:
Copyright 2025 - <Your Name>

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED.

--------------------------------------------------------------------------
This script blinks the BeagleBone's USR3 LED at 5Hz.
--------------------------------------------------------------------------
"""

import Adafruit_BBIO.LED as LED
import time

# Initialize the LED
led = LED.LED("USR3")

try:
    while True:
        led.on()
        time.sleep(0.1)   # 0.1s ON
        led.off()
        time.sleep(0.1)   # 0.1s OFF
except KeyboardInterrupt:
    led.off()
    print("Exiting blink script.")
