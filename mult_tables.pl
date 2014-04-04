#!/usr/bin/perl
# Multiplication Table problem
# This creates a 12 x 12 multiplication table with hypen delmiters.  I got the idea from an article about interview questions for DevOps guys.

for($i=1;$i<=12;$i++){ 
foreach(1..12) {
$val = $i * $_; print $val; if($val < 10){$sep = "----"}elsif($val >=10 && $val < 100){$sep = "---"}else{$sep = "--"};
print $sep unless $_ >= 12;
}
print "\n";
}
