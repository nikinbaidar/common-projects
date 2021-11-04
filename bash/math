#! /bin/bash
# Filename: math

function isOption() {
    firstChar=$(echo $1 | cut -c 1)
    test "${firstChar}" = "-"
    return $?
}

function countValues() {
    count=0
    for parameter in $@ ; do
        if isOption ${parameter} ; then
            break
        else
            ((count++))
        fi
    done
}

function inRange() {
    # inRange -min x -max y test_argument
    lower_bound=$2
    upper_bound=$4
    count=$5
    ! [[ ${count} -lt ${lower_bound} || ${count} -gt ${upper_bound} ]]
    return $?
}

function add() {
    num1=$1
    num2=$2
    sum=$((${num1} + ${num2}))
    echo $sum
}

function multiply() {
    product=1
    for (( i=1 ; i <= ${count} ; i++ )) {
        currentNumber=${!i}
        product=$(( ${product} * ${currentNumber} ))
    }
    echo ${product}
}

until [ -z "$1" ] ; do
    currentParameter="$1"
    case ${currentParameter} in

        -a) shift
            numberOfValuesAccepted=2
            countValues $@
            if [ ${count} -eq ${numberOfValuesAccepted} ]
            then
                add $1 $2
            else
                echo "$0: option 'a': 2 arguments required ${count}" \
                    "were provided"
            fi
            ;;

        -m) shift
            countValues $@

            if inRange -min 2 -max 4 ${count}
            then
                multiply $@
            else
                echo "$0: option 'm': 2 to 3 values are required" \
                    "${count} were provided"
            fi
            ;;

        *) shift ;;

    esac
done
