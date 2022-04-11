# Pi-Relay-Sunrise-light
this service will turn on the light at sunrise using Pi-Relay-Server

## Setup
## you will need to set your location in conf.py
###go to https://gml.noaa.gov/grad/solcalc/ and look at the location field there site helped me figure out my lat/long and utc offset

`sudo cp suntracker.service /etc/systemd/system/` 
`sudo systemctl daemon-reload`
`sudo systemctl enable suntracker.service`
`sudo systemctl start suntracker.service`
`sudo systemctl status suntracker.service`
