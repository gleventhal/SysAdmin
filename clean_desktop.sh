#!/bin/bash
###############################
# Clean Desktop               #
# by Gregg Leventhal Jan 2014 #
###############################

cd ~/Desktop
suffixes=(
$(ls -1d *.*|while read i;do echo ${i##*.};done|sort -u)
)

for suffix in ${suffixes[@]}
do
	mkdir ./${suffix}
	mv *.${suffix} ./${suffix}
done

