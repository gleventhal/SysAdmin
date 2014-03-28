#!/bin/bash
#
# crontab * * * * * webapp-watchdog.sh
# description: watchdog service for web site
# processname: webapp-watchdog.sh
#
# Set debug to 0 for production. Any other value will set debug.  
# If the first argument to the script matches debug (debug, -debug, --debug), debugging is turned on.
touch /tmp/ww.cron
APACHECTL=$( find /opt -name apachectl)

[[ $1 =~ "debug" ]] && DEBUG=1 || DEBUG=0 
[[ ${DEBUG} -ne 0 ]] && set -x

URL=""
HOST=
SEARCHSTRING=""
MAILTO=""
TEMPFILE=/tmp/webapp-watchdog.feed

# path to nagios plugins for check
PLUGINPATH=/oac/sfw/nagios/libexec

# If tempfile exists, exit because a restart is in progress.  If it exists after 15 consecutive runs then remove it so the next
# run will not exit prematurely.  In this case it was probably left from a run that was ended before the tempfile was cleaned.

if [ -f ${TEMPFILE} ]; then
	echo "- - -" > ${TEMPFILE}
	if [[ $( wc -l ${TEMPFILE}) > 15 ]]; then
		rm -f ${TEMPFILE}
	fi
	exit
fi

check_process() {
	OUTPUT=$(${PLUGINPATH}/check_http -w 5 -c 10 -u ${URL} -s "$SEARCHSTRING" -H ${HOST})
}


restart_apache() {
	touch ${TEMPFILE}
	$APACHECTL -k restart		
	rm -f ${TEMPFILE}
}

# Check for 200 OK on the Feed URL; On Error, log to syslog and restart Apache.  If Apache fails to restart, notify us via email.
check_process || { logger "WEBAPP ERROR - ${HOST} error - ${OUTPUT}"; restart_apache && echo "Watchdog: Apache was restarted"|mail -s "${HOST} Service Restart" ${MAILTO} || echo "There was an error restarting Apache on ${HOST}"|mail -s "Error - ${HOST}" ${MAILTO} ; }

[[ $1 =~ interactive ]] && echo ${OUTPUT}
