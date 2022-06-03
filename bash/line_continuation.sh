#! /bin/bash

count=0
range=(216 218 219 227)

# for i in ${range[@]} ; do
#   echo ${range[$count]}
#   ((count++))
# done

echo $args

for ((i=0; i<5; ++i)); do
    args+=($i)
    # echo "${args[@]}"
done

echo ${args[@]}
