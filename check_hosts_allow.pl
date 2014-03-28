#!/usr/bin/perl
#################################
#	check_hosts_allow.pl        #
# Gregg Leventhal for WCMC 2014 #
#################################

my $IP = $ARGV[0];
my $FILE = '/etc/hosts.allow';
my $TEMPFILE = '/etc/hosts.allow.TEMP';

# Make sure it is an IP with either 157. or 140. as first octet
unless ( $IP =~ qr/(140|157)\.(\d{1,3}\.){2}\d{1,3}/ ) {	
	die "Usage: $0 IP Address\n";
} else {		
	open FH2, ">", $TEMPFILE;
	open (FH, "<", "$FILE");    	
foreach $LINE (<FH>) {      	
	if ( $LINE =~ qr/^sshd: (.*)/i ) {          	
		@LIST = split(", ", $1);
		foreach (@LIST) {               	
			chomp $_;
			$_ =~ s/\s//g;               		 
			if( ($IP eq $_) || ($IP =~ /^\Q$_/) )  {
			print "IP ADDRESS: $IP found! \n";                     
			exit 0;
			} else {                 		
				$NEWLIST .= "$_, " }
				} print FH2 "sshd: $NEWLIST$IP\n";
			} else { print FH2 "$LINE" };      			 
		} 
	rename $TEMPFILE, $FILE;   		
	}
	print "$IP has been added to $FILE\n";
	close $FH;
if( -e "$TEMPFILE") {
	unlink "$TEMPFILE";
}
