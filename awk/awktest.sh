
clear

sensors | awk ' /^Core/ { print } ' | awk ' BEGIN { a = 0; OFS=""; ORS=" ";
print "Temp:"};
 {
    # { print a }
    if ( a == 0 ) {
        ORS = " | "
    }
    else {
        ORS = "\n"
    }
 };
{ print $3 };
{ a = 1 } '
