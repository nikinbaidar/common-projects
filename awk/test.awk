BEGIN {
    count = 0 ;
}

{ if ( count < 10 )
    {
    print "\n"  ;
    count++;
}
}


