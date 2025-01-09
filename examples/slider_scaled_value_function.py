# SPDX-FileCopyrightText: 2025 Jose David M.
#
# SPDX-License-Identifier: MIT
#############################
"""
This example demonstrates the use of the Slider class to control the brightness of the display
"""

import time
import board
import displayio
import adafruit_touchscreen
from slider import Slider

display = board.DISPLAY

ts = adafruit_touchscreen.Touchscreen(
    board.TOUCH_XL,
    board.TOUCH_XR,
    board.TOUCH_YD,
    board.TOUCH_YU,
    calibration=((5200, 59000), (5800, 57000)),
    size=(display.width, display.height),
)

# Create the slider
my_slider = Slider(20, 30, minimum_value=0.0, maximum_value=1.0)

my_group = displayio.Group()
my_group.append(my_slider)

# Add my_group to the display
display.root_group = my_group

# Start the main loop
while True:
    p = ts.touch_point  # get any touches on the screen
    # Check each slider if the touch point is within the slider touch area
    if p:
        if my_slider.when_inside(p):
            my_slider.when_selected(p)
            display.brightness = my_slider.corrected_value
    # touch response on PyPortal is more accurate with a small delay
    time.sleep(0.05)
