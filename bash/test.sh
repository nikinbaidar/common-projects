#! /bin/bash

clear

declare i=0

while echo $i
    [ $i -lt 10 ]
do
    (( i++ ))
done
