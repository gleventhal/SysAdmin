#!/usr/bin/perl 
my $count = 1; my $a = 0; my $b = 1;
print "$a\n";
print "$b\n";
while ( $count < 50 ) {
	$sum = $a + $b;
	print "$sum\n";
	$a = $b;
	$b = $sum;
	$count += 1;
}
