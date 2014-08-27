#!/usr/bin/perl
# A totally inefficent version of Tail in Perl.. Soon to come, and efficient version
use strict;
use warnings;

our $FILE = $ARGV[0] || die "Usage $0 File Name\n";
our $COUNT = 0;
open(FH, $FILE) or die "Cannot open File: $FILE\n";

foreach my $line (<FH>) {
    $COUNT++;
}

close(FH);
our $LENGTH = $COUNT;

our $NEWCOUNT = 0;
open(FH, $FILE) or die "Cannot open File: $FILE\n";
foreach my $line (<FH>) {
    $NEWCOUNT++;
    next unless ($NEWCOUNT >= ($COUNT - 9));
    print $line;
}

close(FH);
