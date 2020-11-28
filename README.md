# Janssen AIBT Operations Manual

**Janssen AIBT** is the Bluetooth Android app for Janssen's one-press patient-controlled injectors. This is meant to be used in conjunction with a Raspberry Pi 'Zero W', which is running the Python scripts located in the repository: https://github.com/elb5465/Janssen_AIBT. There, you will also find this manual and the Android app download (the '.apk' file). Alternatively, these files can be downloaded and saved remotely in another storage provider like Google Drive or Box.


# 

## How to Install the Android App

1. Go to a browser on the phone and locate the '.apk' file using the link above, or any other platform you may have saved it to. 
2. Download the '.apk' file onto the phone.
3. You will be prompted to install the app, continue to do so.

### Trouble-Shooting:

If your browser does not allow you to download applications from the internet, try the following:

**From *nextpit.com*:** "*How to install apps from outside the Google Play Store*"
1. Go to Settings.
2. Find the Security & privacy option and tap on it.
3. Scroll down and look for 'install from unknown apps'. If it's not there, try under 'more'.
4. You should be presented with a list of apps. Find your browser - Chrome, for example.
5. Tap on it and then select 'Allow from this source'.

If the above path doesn't work for you, try the following:

1. Head to Settings.
2. Go to Apps & notifications and then select configure apps.
3. Scroll down. Find and tap advanced options or special app access.
4. Scroll to the bottom of the special app access menu, where you can find the Install unknown apps option.
5. Find your browser, (e.g. Chrome), tap it and select Allow from this source.



## How to Use

1. **Turn on the Raspberry Pi:**  Connect the Raspberry Pi via micro-USB to a  power supply of around ***5V*** and it will power on and begin running the necessary programs automatically (Most portable battery packs are suitable for this, but check their specifications).
2. **Go to settings** and **select Bluetooth settings** (On the Android phone)
3. **Tap 'Pair new device'** and **select the Raspberry Pi** 
(May take a minute for the device to show up if the Raspberry Pi was just powered on)
5. **Open the Janssen AIBT Android app**.
(The paired device should now be displayed at the top of the homescreen.)
6. **Tap the device to connect** and follow the in-device instructions to step through the app. 
If you want to continue to the instructions **without connecting to the device**, you can just click the 'next' arrow to step through the app without sending signals to the Raspberry Pi.
8. **To turn off the Raspberry Pi:** Find the attached button and **hold it down for 3 seconds**. You should see the green light on the Raspberry Pi begin to blink about 10 times and then disappear. At that point **unplug the power supply from the Raspberry Pi**.

