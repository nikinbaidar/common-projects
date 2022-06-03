#!/usr/bin/env bash

device_address=0 

while [ ${device_address} -le 2 ] ; do
  if ping -c 1 192.168.1.${device_address} &> /dev/null
  then
    echo 192.168.1.${device_address}
  fi
  ((device_address++))
done
