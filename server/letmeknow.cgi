#!/bin/bash
#requests: exit: exitstatus of scripts. name: name of the process. fetch: fetch the exit status
#responses: retval: retval of this script, data: html data.

function invalid_request {
 echo "retval:" $1
 echo "data: Invalid Request"
}

function update_exit_status {
 echo $2 > ./${4}.status
 echo "retval: 0"
 echo "data: Exit status updated"
}

function fetch_status {
 filenames=( $(ls *.status ) )
 
 for element in $(seq 0 $((${#filenames[@]- 1})))
 do
   st=`cat ${filenames[$element]}`
   data="$data ${filenames[$element]} $st"
   rm ${filenames[$element]}
 done
 echo "retval: 0"
 echo "data: " $data
}

echo "Content-type: text/plain"
echo ""
query=( $(echo $QUERY_STRING | tr "=&" " ") )


if ( [[ ${#query[@]} -ne 4 &&  $REQUEST_METHOD == "POST" ]] || [[ ${#query[@]} -ne 1 &&  $REQUEST_METHOD == "GET" ]] )
then
 invalid_request "-1"
 exit
fi

case ${query[0]} in
exit)
  update_exit_status ${query[@]}
  ;;
fetch)
  fetch_status
  ;;
*)
  invalid_request "-1"
  ;;
esac

