num=${!#}

until [ -z "$1" ] ; do
  case $1 in
    -min) shift
      minval=$1
      ;;
    -max) shift
      maxval=$1
      ;;
    *) 
      shift

      ;;
  esac
done

if [[ ${num} -gt ${minval} && ${num} -lt ${maxval} ]] ; then
  echo True
else
  echo False
fi
