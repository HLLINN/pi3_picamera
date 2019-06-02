# Capturing photos automatically every five second and shutdown after done with finish capturing 400 pieces photos 

### Device Requirement:

**1. Raspberry Pi3 B+ or Raspberry Pi Zero W**

**2. 8MP Raspberry Pi NoIR Camera Module(v2)**

**3. Official Case for Raspberry Pi Zero W (Selective)**


### STEPs:

**1. `$sudo apt-get update`**<br/>
     `$sudo apt-get intall python-picamera python3-picamera`**<br/>
     or`$sudo pip install picamera`**<br/>

**2. Create a python program "pi3_picamera.py"**

**3. The last step is that: `$sudo nano ~/.config/lxsession/LXDE-pi/autostart` Then add a line of script: `@sh /home/pi/pi3camera/picamera.py`**

**4. Finally, restart your Raspberry Pi Zero W to test the working status of this function.  `$sudo reboot`**


### Reference:

1.[How To Send A Captured Image Through Email Using Raspberry Pi, Pi Camera, And Python](https://www.c-sharpcorner.com/article/how-to-send-the-captured-an-image-through-the-mail-using-raspberry-pi-and-python/)
<br/>
2.[picamera__official website](https://picamera.readthedocs.io/en/release-1.10/api_camera.html)
<br/>
3.[HOW TO STREAM THE PICAMERA TO YOUR BROWSER](https://desertbot.io/blog/how-to-stream-the-picamera)
<br/>

