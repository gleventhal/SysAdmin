#!/bin/bash
# Words With Enemies
# Reddit programming challenge /r/dailyprogrammer
# Takes Two words as arguments and collides them removing any duplicate letters; The longest remaining word wins

LEFT_SCALAR=$1
LEFT=($(echo $1|sed 's/./& /g'))
RIGHT=$2
VALLEY=()

for L in ${LEFT[@]}; do
	[[ $RIGHT =~ $L ]] && { RIGHT=$(echo $RIGHT|sed "s/$L//");LEFT_SCALAR=$(echo $LEFT_SCALAR|sed "s/$L//") VALLEY+=($L); }
done

LEFT=($(echo $LEFT_SCALAR|sed 's/./& /g'))
RIGHT=($(echo $RIGHT|sed 's/./& /g'))

LLENGTH=${#LEFT[@]}
RLENGTH=${#RIGHT[@]}

if [[ $LLENGTH > $RLENGTH ]]; then
	echo LEFT WINS WITH $(echo ${LEFT[@]}|sed 's/ //g')!
elif [[ $RLENGTH > $LLENGTH ]]; then
	echo RIGHT WINS WITH $(echo ${RIGHT[@]}|sed 's/ //g')!
else
	echo TIE!! 
fi
