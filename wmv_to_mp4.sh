#!/bin/bash
[[ -z "$1" ]] && { printf "Usage: $(basename $0) <dir>\n"; exit 1 ; }

dir="$1"

spaces_to_underscore() 
{
    for i in *.wmv
    do 
        mv "$i" $(echo "$i" |tr ' ' _)
    done
}

move_wmv()
{
    mkdir "${dir}_wmv"
    OLDIFS=$IFS
    IFS='
'
    mv ${dir}/*.wmv "${dir}_wmv"
    IFS=$OLDIFS

main()
{
    cd "$dir"
    spaces_to_underscore
    ls | egrep -q '\.mp4'
    if [[ $? -eq 0 ]]; then
        printf "You already have mp4 files in this directory\n"
        printf "Continuing in 5 seconds, hit Ctrl C to stop\n"
        sleep 5
    fi
    for i in *.wmv
    do 
        ffmpeg -i "$i" -c:v libx264 -crf 23 -c:a aac -q:a 100 \
        -strict -2 $(echo $i| sed 's/.wmv/.mp4/')
    done
}

main
move_wmv
