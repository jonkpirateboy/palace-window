# Palace Window

A python script that changes the light of a [Wiz bulb](https://www.wizconnected.com/en-ca/products/bulbs) depending on the weather.

## Install

Install a [Raspberry Pi OS](https://www.raspberrypi.com/software/) on a [Raspberry Pi](https://www.raspberrypi.com/products/), no desktop environment needed. I suggest enabling SSH.

Once set up, log in to the computer through SSH, or some other method if you didn't enable SSH.

Run the following commands to make sure everything is up to date:

`apt-get update`

`apt-get upgrade`

Install pip:

`sudo apt install python3-pip`

Install [Python weather](https://github.com/null8626/python-weather)

`pip install python-weather`

Put the file `palace-window.py` file and the `palace-window-config` directory in your `home` directory of your pi.

Create an account on https://www.meteosource.com/ for the weather API used in the script. I suggest using the Free subscription plan. Add your API key in the `palace-window-config/key.txt` file.

Turn on your Wiz bulb and activate it through their app. Add the IP address for the bulb in the `palace-window-config/ip.txt` file. For example you can do that with the `arp -a` command on Mac or from the pi.

Change the city in the `palace-window-config/city.txt` file to what you want the bulb to reflect.

### Autostart

If you want the script to start automatically when the pi is booted run this command:

`crontab -e`

Answer `1`

Add this to the file:

`@reboot /bin/sleep 30; /usr/bin/python /home/<your home directory>/palace-window.py`