#!/bin/bash

# I am creating a variable greeting


greeting='Hello World'

# I am printing the contents of greeting

echo $greeting

# touch and print a range of files in a loop

for myfile in {A..Z}.tx;
do
    touch $myfile
    echo $myfile
done 
