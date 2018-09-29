# Logitech G910 G-Keys for Ubuntu / Mint

Install these required packages

`sudo apt install python-pip libudev-dev hidraw nano
sudo -H pip install setuptools python-uinput pyudev`

Copy g910-gkey-uinput.py to a folder of your liking.
Start in a terminal with `python /path/to/g910-gkey-uinput.py` to see if it's working for you

Adding a systemd service unit
`sudo nano /lib/systemd/system/g910keys.service`

Paste this inside, change the path to match your system 
`[Unit]
Description=Logitech G910 G-Keys
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /path/to/g910-gkey-uinput.py

[Install]
WantedBy=multi-user.target`

Press Ctrl + X to exit nano and save the file.

Then issue these commands to start the G-Key script as a service.
`sudo systemctl daemon-reload
sudo systemctl enable g910keys.service
sudo systemctl start g910keys.service`
