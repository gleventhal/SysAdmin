# Get All hosts from Foreman and use regex/substring matching to ssh to any host
ping -c 1 $FOREMAN_HOST > /dev/null
if [[ $? == 0 ]]; then
        servers=($(mysql -h$FOREMAN_HOST -u$FOREMAN_USER -p$FOREMAN_PASS\
        foreman -e 'SELECT name from hosts' 2>/dev/null))
fi


function s()
{
  matches=()
  [[ $2 = 'print' ]] && prn=True
  if [ -z $1 ]; then
      printf "%s\n" ${servers[@]}
  else
      for i in  ${servers[@]}; do
          [[ $i =~ $1 ]] &&  matches+=($i)
      done
      if [[ ${#matches[@]} -eq 1 ]]; then
          ssh ${matches[@]}
      else
          for((i=0;i<${#matches[@]};i++)); do
              if [[ $prn = 'True' ]]; then  printf "%s\n" "${matches[$i]}"; else
              printf "%s\n" "$((i + 1)):    ${matches[$i]}" ; fi
          done
          printf "%s\n" "Choose a server to connect to:"
          read num
          if [[ $num != '' ]]; then
              ssh ${matches[$((num - 1))]}
          fi
      fi
  fi
}
