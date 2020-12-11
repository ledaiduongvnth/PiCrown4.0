#!/bin/bash

NEW_IP_SUFFIX=13
NEW_CAM_IP_SUFFIX=3
NEW_BASE_IP=10.61.212.

NEW_ROUTER_IP=$NEW_BASE_IP'1'

NEW_IP=$NEW_BASE_IP$NEW_IP_SUFFIX

NEW_CAM_IP=$NEW_BASE_IP$NEW_CAM_IP_SUFFIX


OMXPLAYER_FILE='/home/pi/Desktop/App/deployment/omxplayer.service'
DHCP_FILE='/etc/dhcpcd.conf'
CONFIG_FILE='/home/pi/Desktop/App/config.py'

sudo sed -i 's/abcd1234@.*:554/abcd1234@'$NEW_CAM_IP:554/g $OMXPLAYER_FILE

sudo sed -i 's/.*static ip_address.*/static ip_address'=$NEW_IP/g $DHCP_FILE
sudo sed -i 's/.*static routers.*/static routers='$NEW_ROUTER_IP/g $DHCP_FILE

sudo sed -i 's/.*BASE_IP.*/BASE_IP='\'$NEW_BASE_IP\'/g $CONFIG_FILE
sudo sed -i 's/.*MY_IP_SUFFIX.*/MY_IP_SUFFIX='$NEW_IP_SUFFIX/g $CONFIG_FILE

sudo sed -i 's/.*/display'$NEW_IP_SUFFIX/g /etc/hostname

sudo sed -i 's/.*127.0.1.1.*/127.0.1.1      display'$NEW_IP_SUFFIX/g /etc/hosts

sudo cp $OMXPLAYER_FILE /etc/systemd/system

/home/pi/Desktop/App/deployment/enable_services_on_boot.sh

sudo reboot