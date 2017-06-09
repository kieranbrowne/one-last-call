# [One Last Call](https://www.onelastcall.com/)



## Setup

### Cron
```
sudo apt-get install gnome-schedule
crontab -e
... then add the following line
@reboot python /path/to/booth.py &
```
