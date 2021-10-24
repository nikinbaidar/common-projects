#! /bin/bash
# factorial.sh
# Compute the factorial of 1st positional parameter.

factorial=1

for (( i = $1 ; i >= 1 ; i-- ))
do
    factorial=$(( $factorial*$i ))
done

echo ${factorial}
