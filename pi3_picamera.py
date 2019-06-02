#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()
#camera.rotate = 180 # the rotation definition
#camera.resolution = (1920, 1080)
#camera.framerate = 15  # simultaneously exists with 1920x1080 definition
#camera.resolution = (60, 60) # the minimum definition
#camera.resolution = (2592, 1944) # the maximum definition
#camera.framerate = 15  # simultaneously exists with the maximum definition
camera.start_preview()
camera.brightness = 50 #range:0~100 , default:50
camera.contrast = 50 #range:0~100, default:50
camera.awb_mode = "auto"  #off,auto,sunlight,cloudy,shade,tungsten,fluorescent,incandescent,flash,horizon
camera.exposure_mode = "auto" #off, auto,night,nightpreview,backlight,spotlight,sports,snow,beach,verylong,fixedfps,antishake,fireworks
sleep(3)
timenow = (time.strftime("%y-%b-%d_%H:%M:%S"))
camera.capture("/home/pi/picamera_file/"+timenow+".jpg")
#camera.capture("/home/pi/picamera_file/image.jpg")

camera.stop_preview()

print("Exit the program")
