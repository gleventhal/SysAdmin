#!/usr/bin/perl

use warnings;
use strict;
use Mail::Sendmail;

chomp(my $svr = `hostname`);
my @output = `df -h`;
my $msg;
my $mailto = 'baz@bar.com';
my $threshold = 90;

sub main
{
  foreach (@output) { 
      if ( m/(\d+)% (.*)/ &&  $1 > $threshold) {
          $msg .= "$svr: $2 volume  is $1 percent full\n" 
      } 
  }

  my %mail = ( To      => $mailto,
               From    => 'foo@bar.com',
               Subject => "$svr has a full file system",
               Message => $msg
             );

  if ( $msg ) { 
       sendmail(%mail) or die $Mail::Sendmail::error;
  }
}

main
