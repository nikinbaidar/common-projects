#!/bin/sh

# The inspiration for the name of this application came from
# [here](https://bit.ly/3fQ3Wo3) and [here](https://bit.ly/3WK4YSZ).

function openFilePickerDialog() {


    function showArtWork() {
        [[ -f ${DOTS}/shell/prompt_colors ]] \
            && source ${DOTS}/shell/prompt_colors

        echo -e "${p}" 
        echo -ne "Lehte" | figlet -f pagga 
        echo 
    }


    function createNewFile() {
        echo -en "\n:: Enter new filename: ${_g}${input}" 
        read filename
        input="${input}""${filename}"
        # Just in case user decided to add a sub directory in path.
        sub_dir=$(echo "${input}" | awk 'BEGIN { FS = "/" } {
        for(i=1; i<NF; i++) 
            printf $i"/"
        }')
        if ! [ -d "${sub_dir}" ]; then
            mkdir "${sub_dir}"
        fi
        touch "${input}"
    }


    function extendFilePickerDialog() {
        input="${1}/"
        echo -e "(1) Create new file (2) Open selection in lf \n"
        echo -en ":: Do you want to create new file in '${input}' ? [Y/n] "
        read response
        if [ "${response}" == "2" ]; then
            lf "${input}"
        elif [ "${response}" != "n" ]; then
            createNewFile 
        fi
    }


    showArtWork
    input=$(fzf)
    [[ -d "${input}" ]] && extendFilePickerDialog "${input}"
    echo ${input} > /tmp/temporaryfile.txt
}
export -f openFilePickerDialog


st -c "File Picker" -T "Lehte - Terminal File Picker"\
    -g 90x25+325+120 sh -c 'openFilePickerDialog'

if [ -f /tmp/temporaryfile.txt ] ; then
    x=`cat /tmp/temporaryfile.txt`
    rm -f /tmp/temporaryfile.txt
fi

echo "${x}"
