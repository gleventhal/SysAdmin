#!/usr/bin/perl

use warnings;
use strict;
use Mail::Sendmail;

my $svr = `hostname`;
my @output = `df -h`;
my $msg;
my $mailto = 'someone@foo.com';
my $threshold = 90;

sub main
{
  foreach (@output) {
    if (($_ =~ m/(\d+)% (.*)/) && ( $1 > $threshold )) {
      chomp($svr); $msg = "$svr: $2 volume  is $1 percent full\n" }
    }

    my %mail = ( To      => $mailto,
                 From    => 'Server@foo.com',
                 Subject => "$svr has a full file system",
                 Message => $msg
               );

  if ( defined $msg ) {
    sendmail(%mail) or die $Mail::Sendmail::error;
  }

}

main
