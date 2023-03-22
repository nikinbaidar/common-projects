#!/bin/bash

function working {
  echo -e "${R}Enter the directory to create file:"
  directory=$(fzf)
  echo The file will be created in $directory
  echo "Enter filename:"
  read x
  touch ${directory}/${x}
  sh -c "echo_reverse bar fo\ o"
  fzf | xargs -I % bash -c 'echo_reverse bar %'
  echo -e "\b$(fzf)" | xargs echo -e "something"
  echo "$(fzf)/" | xargs -I % bash -c 'echo -e % "\bsomething"'
}

# read filename && echo Input: ${filename}
# fzf # | xargs echo hidden

function echo_reverse() {
  for i in "$@"; do echo -e "$i" ; done | tac | tr '\n' ' '
  echo
}
export -f echo_reverse


function read_and_write() {
  echo $d
  read filename
  echo ${1}/${filename}
}

echo -e "${R}Enter the directory to create file:\n"
d=$(fzf)
clear -x 
echo -e "Enter the filename:\n "
echo -n $d/
x=$(read_and_write $d)
echo $x

# sh -c "read_and_write foo"


