#!/bin/bash -f
# Rev in Bash
while read data; do
  word=($(echo $data|tr ' ' '_'|sed 's/./& /g'))
  new=()
  i=$((${#word[@]} - 1))
  while [[ $i -ge 0 ]]; do
    new+=(${word[$i]})
    (( i-- ))
  done
echo ${new[@]}|tr -d ' '|tr '_' ' '
done
