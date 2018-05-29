#!/bin/bash

# touch and print a range of files in a loop

for myfile in {A..Z}.txt;
do
    touch $myfile
    echo $myfile
done 
