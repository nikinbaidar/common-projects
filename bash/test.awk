BEGIN {
    nine = 9 ;

    even[0] = 0
    even["secondEvenNumber"] = 2
    even[nine] = 4
    even[7] = 6
    even[666] = 8
}

{ print "The length of the array is", length(even) }
