# [One Last Call](https://www.onelastcall.com/)



## Setup

### Cron
```
sudo apt-get install gnome-schedule
crontab -e
... then add the following line
@reboot python /path/to/booth.py &
```

### Terminal
This script requires some terminal utilities
- sshpass
- 

Install the above with
```
apt-get install sshpass
```
