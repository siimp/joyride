**THIS IS IN EARLY DEVELOPMENT**

# Joyride (Joyor) QS-S4 protocol


## Project Setup (linux)
```
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt

```

## Reverse engineering the throttle controller

```
sudo ./venv/bin/python reverse_engineering.py
```

## Running the utility

```
sudo ./venv/bin/python utility.py
```

## Useful information
```
stty --all -F /dev/ttyUSB0 
```

https://pyserial.readthedocs.io/en/latest/shortintro.html  
https://electricbike.com/forum/forum/kits/bafang-mid-drives/36793-bbsxx-serial-communication-protocol  
https://github.com/philippsandhaus/bafang-python  
https://www.joyorscooter.com/user-manual  
https://electric-scooter.guide/guides/qs-s4-lcd-throttle  
