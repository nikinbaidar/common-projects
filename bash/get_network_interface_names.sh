#!/bin/sh

net_interface_names=$(ip link show | awk ' /^[1-3]/ { x = length($2) - 1 ; print substr($2, 1, x) }')
for item in ${net_interface_names} 
do
  echo $item
done
