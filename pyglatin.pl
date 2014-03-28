#!/usr/bin/perl

use warnings;
use strict;

sub translate {
my $word = shift;
$word = lc $word;
if ( $word =~ qr/^[aeiou]/) {
    print "$word", "ay ";
    }else{
    $word =~ s/([a-z])([a-z]+)/$2$1/;
    print "$word", "ay ";
    }
}

foreach (@ARGV) {
   translate $_;
};
