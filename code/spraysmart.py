# Run this in OpenMV's IDE on your openMV camera.

import sensor, image, time
from pyb import Pin

threshold_index = 0 # selector for the threshold index

solenoid = Pin('P1', Pin.OUT_PP, Pin.PULL_DOWN)

# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
# List of thresholds. Currently it only uses the first item in the list, but the idea is to
# eventually iterate over the list and look at all the thresholds in the list.
# Find the values using the threshold editor in the OpenMV IDE (Tools -> Machine Vision -> Threshold Editor)
thresholds = [(100, 0, -64, -26, -31, 81), # Currently used thresholds
              (30, 100, 15, 127, 15, 127), # Unused thresholds
              (30, 100, -64, -8, -32, 32), # Unused thresholds
              (0, 30, 0, 64, -128, 0)] # Unused thresholds

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

# Only blobs that with more pixels than "pixel_threshold" and more area than "area_threshold" are
# returned by "find_blobs" below. Change "pixels_threshold" and "area_threshold" if you change the
# camera resolution. "merge=True" merges all overlapping blobs in the image.

solenoid.value(True) # This single relay module is off when High
while(True):
    clock.tick()
    img = sensor.snapshot()
    blobs = img.find_blobs([thresholds[threshold_index]], pixels_threshold=200, area_threshold=300, merge=True)
    for blob in blobs:
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
    solenoid.value(1 if len(blobs) else 0)
