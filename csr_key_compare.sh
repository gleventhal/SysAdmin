#!/bin/bash
# Test if a CSR and Key match each other
# Gregg Leventhal 2014

function exit_fail() 
{
	printf "%s\n" "One or more input files has an unexpected format"
	exit 19
}

function pipe_check()
{
	for RETURN in ${PIPESTATUS[@]}
	do 
		if [[ $RETURN -ne 0 ]]; then 
			exit_fail
		fi
	done
}
# Initialize Input Variables
if ! [ $1 ] && ! [ $2 ]; then
	read -p "Please provide the full path to the CSR file: " CSR
	read -p "Please provide the full path to the KEY file: " KEY
else
	CSR=$1
	KEY=$2
fi

read CSR_MOD < <(openssl req -in $CSR -noout -text|sed -n '/modulus/I,/exponent/Ip'|sed '/^[[:space:]]*[a-zA-Z]\{3,\}:/Id'|sed 's/^ *//g')
pipe_check

read KEY_MOD < <(openssl rsa -in $KEY -noout -text|sed -n '/modulus/I,/exponent/Ip'|sed '/^[[:space:]]*[a-zA-Z]\{3,\}:/Id'|sed 's/^ *//g')
pipe_check

function main() 
{
	printf "%s\n"  "$CSR_MOD"
	echo
	printf "%s\n"  "$KEY_MOD"
	if [[ $(diff <(echo $CSR_MOD) <(echo $KEY_MOD) )x = 'x' ]]; then
		printf "%s\n" "Key and CSR match!"
	else
		printf "%s\n" "Key and CSR Do Not match!"
	fi
}

main
