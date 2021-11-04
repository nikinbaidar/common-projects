function inRange() {
    test_num=$5
    until [ -z "$1" ] ; do
        case $1 in
            -min) shift
                minval=$1
                ;;
            -max) shift
                maxval=$1
                ;;
            *) shift
                ;;
        esac
    done
    ! [[ ${test_num} -lt ${minval} || ${test_num} -gt ${maxval} ]]
    return $?
}

echo -n "Enter a number: "
read input

if inRange -max 4 -min 2 ${input}
then
    echo Yes
else
    echo No
fi
