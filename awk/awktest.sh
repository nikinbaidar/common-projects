
clear

awk '
function square(array) {
    for ( i in array )
        array[i] = array[i]^2;
}

function sum(array) {
    s = 0 ;
    for ( i in array )
        s += array[i] ;
    return s;
}

{
    a[0] = 7;
    a[1] = 2;
    a[2] = 9;
    a[3] = 1;
    a[4] = 0;

}

END {
square(a) ;

b = sum(a) ;
# print b ;

for ( i in a ) {
    print j;
    j++;
}

}

'  /proc/loadavg
