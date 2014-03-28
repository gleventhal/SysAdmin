#!/bin/bash
##################################################################
#																 #
# Assign Hostname To Mac Workstations based on DHCP Reservations #
# Gregg Leventhal 2013		 #														 
#############################################################################################################
#																											#
# infile.txt should look like a list of: hostname<space>ip													#
# either copy the list to the same directory the script is run from											#
# or if using ARD, send the infile.txt to the remote host and edit the script to point to the absolute path #
# Then copy this script into the Send UNIX Command prompt and run as user "root"							#
#############################################################################################################

local_IP=$(ipconfig getifaddr en0) || { echo "No IP on Interface en0\!"; exit 1;}
glean_host=$(grep ${local_IP} infile.txt| cut -d' ' -f1) 

if [ -z ${glean_host} ]; then
	printf "%s\n" "IP Not Found in List!"
	exit 1
fi

	scutil --set HostName ${glean_host}
	scutil --set LocalHostName ${glean_host}
	scutil --set ComputerName ${glean_host}



printf "%s\n" "Computer With IP ${local_IP} was assigned HostName: ${glean_host}"
