#!/bin/bash

# str="/tmp/one/two/three someting/test me.png"
str="/tmp/one/two/three/test me.png"


# Get file extenstion:
# echo ${str} | cut -d . -f 2

# Get parent dir
# echo ${str} | cut -d / -f 1


a=$(echo "${str}" | awk 'BEGIN {FS = "/"} {for(i=1;i<NF;i++) printf $i"/"; print ""}')
b=$(echo "${str}" | awk 'BEGIN {FS = "/"} {print $NF}')

declare -p a
declare -p b

echo 

if ! [ -d "${a}" ]; then
    echo \'${a}\' is created first 
fi

echo \'${b}\' is created in \'${a}\'


        # if [ -f ${filename} ] 
        # then 
        #     echo -en ":: Proceed and overwrite ${filename} ? [Y/n] ${f}" 
        #     read response
        #     if [[ ${response} = "n" ]] ; then
        #         exit 
        #     fi
        # fi

        # echo ${filename} | xargs -I % sh -c 'mv "/tmp/temporary.png" "%" ' # ${filename} is replaced.

        # echo ${input} > /tmp/temporaryfile.txt
