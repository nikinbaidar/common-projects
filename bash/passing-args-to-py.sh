#! /bin/bash

clear

test_var1=1
test_var2=2
test_var3="three"

# Passing a single value:

echo $(python -c "import sys ; print(sys.argv[1])" $test_var1)

# Passing multiple values:

echo $(python -c "import sys ; mylist = (sys.argv[1:]) ; \
    mylist[0] = float(mylist[0]) ; \
    print(mylist)" $test_var1 $test_var2 $test_var3)
