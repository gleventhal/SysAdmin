#!/usr/bin/perl

$FILE = $ARGV[0] || die "Usage: $0 File\n";
@LINES = ();
open(FH, $FILE);

  foreach $line (<FH>) {
    push @LINES, $line;
  }

$LENGTH = @LINES;

foreach (($LENGTH - 10 )..$LENGTH) {
  print $LINES[$_];
}
