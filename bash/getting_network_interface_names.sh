#!/usr/bin/env bash

net_interface_names=$(ip link show | awk ' /^[1-3]/ { x = length($2) - 1 ; print substr($2, 1, x) }')

echo "The names of the network interfaces:"

for item in ${net_interface_names} 
do
  echo $item
done

echo ""
echo "Corresponding IPs:"

for item in ${net_interface_names} 
do
  echo $item, $(${item})
done

