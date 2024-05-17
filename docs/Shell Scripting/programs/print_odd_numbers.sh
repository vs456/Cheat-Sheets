#!/bin/bash
$i=1
while [[ $i -le 100 ]] ; do
    if [[ $((i % 2 )) == 1 ]] ;then
        echo $i
    fi
    (( i += 1 ))
done