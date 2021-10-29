#! /bin/bash

function len() {
    length=$( echo -n "$1" | wc -m )
    return ${length}
}

clear

echo Enter a word:
read word

len "${word}"
length=$?

echo Length of ${word} is ${length}

for charcater in $(seq 1 ${length}) ; do
    echo ${word} | cut -c ${charcater}
done
