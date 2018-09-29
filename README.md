# Logitech G910 G-Keys for Ubuntu / Mint

Install these required packages

`sudo apt install python-pip libudev-dev nano`

`sudo -H pip install setuptools python-uinput pyudev`

Copy g910-gkey-uinput.py to a folder of your liking.
Start in a terminal with `python /path/to/g910-gkey-uinput.py` to see if it's working for you.

-----------------------------------------------------
Adding a systemd service unit to autostart the G-Keys
`sudo nano /lib/systemd/system/g910keys.service`

Paste the content of the file g910keys.service inside, change the path to match your system 

Press Ctrl + X to exit nano and save the file.

Then issue these commands to start the G-Key script as a service.

`sudo systemctl daemon-reload`

`sudo systemctl enable g910keys.service`

`sudo systemctl start g910keys.service`
