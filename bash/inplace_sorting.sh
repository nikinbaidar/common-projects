#!/bin/sh

a=$(xdotool search --onlyvisible --name firefox)
w=( $( for x in ${a[@]}; do echo $x; done | sort --reverse) )
echo ${w[@]}
