#!/bin/bash
#
# chkconfig: 2345 90 10
# description: Service for Confluence Wiki
# processname: confluence
# By Gregg Leventhal 12/12/13

SHUTDOWNCMD=/oac/confluence/atlassian-confluence-4.3.1/bin/shutdown.sh
STARTUPCMD=/oac/confluence/atlassian-confluence-4.3.1/bin/startup.sh

on_error() {
logger $0 failed 
}

trap "on_error" ERR

usage() {
cat << EOF

`basename $0`: Send a Signal to Confluence
Usage: `basename $0` (stop|start|restart)


EOF
exit 1
}

if [ $# -ne 1 ]; then
        usage
fi

case "$1" in
	stop)
	    echo "Stopping Confluence"
	    ${SHUTDOWNCMD}
	    ;;
	start)
	    echo "Starting Confluence"
	    ${STARTUPCMD}
	    ;;
	restart)
		# Stop Confluence, wait 10 - then check, wait another 110 seconds - check again, if it hasn't quit by then, send a sigkill.  
		#Give it another 2 minutes, if it still doesn't die, return an error
		
	    echo "Restarting Confluence"
	    
	    ${SHUTDOWNCMD}
		sleep 10
		if [ -z $(pidof java) ]; then
			${STARTUPCMD}
		else
			sleep 110
			[[ -z $(pidof java) ]] && ${STARTUPCMD} || kill -9 $(pidof java)
		fi
		count=0
		while [[ x`pidof java` != "x" && count -lt 60 ]]; do
			sleep 2
			let $((count++))
		done
		if [ ${count} -lt 60 ]; then
			${STARTUPCMD}
		else
			exit 2
		fi
	    ;;
	status)
		echo "Confluence is running with PID: $(/sbin/pidof java)"
	    ;;

	*)
	    usage
	    ;;
esac

