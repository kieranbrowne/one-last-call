# [One Last Call](https://www.onelastcall.com/)



## Setup

### Cron
```
sudo apt-get install gnome-schedule
crontab -e
... then add the following line
@reboot ./path/to/runbooth.sh &
```

### Saving to Cloud
To save to the cloud you'll need to set up an ssh key from the pi on the host machine.

### Hardware

#### Preamp
- Connect the dc power cable
- Take the thick black cable from the phone and connect into Phono Left
- Switch "Input Select" to Phono
- Turn volume to full

#### Wifi Dongle
- Just put it in one of the usb slots

#### USB Sound Card
- Insert into remaining usb slot
- Insert one end of aux cable into the part with a picture of headphones and the other end into "Ear In" on the phone.
- Connect the left output of the preamp to the part of the sound card with a picture of a microphone. I found I had to pull the cable out just a tad to make this work.

#### External Board
- Use black ribbon cable to connect the Raspberry Pi (1) to the external board.

#### Magnetic switch
- Red end goes into pin 18 in the raised section on the external board
- Other end goes into any of the GND pins

