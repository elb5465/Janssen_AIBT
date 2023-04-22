# In the RPi, do “nano /etc/rc.local” and add the following line above the “exit(0)” command to start the main script in the background:
# python3 <filepath/YOURfilename.py> &
# --------------------------------------------------------------------------

from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'poweroff'])

# one leg of button should be connected to GPIO 21 (AKA pin40), other on GRND (pin39).
# When someone holds button for 3 seconds, the power off command will shutdown the Pi.

shutdown_btn = Button(21, hold_time=3)
shutdown_btn.when_held = shutdown

pause()

