# Logitech G910 G-Keys for Ubuntu / Mint

To use this script to make use of alternatively mapped G-keys, you need to install the g810-led command line LED controller.
https://github.com/MatMoul/g810-led

Use the command line to configure colors etc., but the most important part is to deactivate the standard mapping of the G- and M-keys. Issue following command to achieve that:

`g910-led -gkm 1`

-----------------------------------------------------
Then install these required packages

Python 2
`sudo apt install python-pip libudev-dev nano`

`sudo -H pip install setuptools python-uinput pyudev`

Python 3
`sudo apt install python3-pip libudev-dev nano`

`sudo python3 -m pip install setuptools python-uinput pyudev`

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
