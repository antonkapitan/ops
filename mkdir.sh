#!/bin/bash

function mk(){
    local RANDOM_MANTH=$(shuf -i 1-12 -n 1)
    LENGM=$(expr length "$RANDOM_MANTH")
    if [[ $LENGM == 2 ]]; then
        MON="$RANDOM_MANTH"
    else
        MON="0$RANDOM_MANTH"
    fi
    local RANDOM_DAY=$(shuf -i 1-31 -n 1)
    LENGD=$(expr length "$RANDOM_DAY")
    if [[ $LENGD == 2 ]]; then
        DAY="$RANDOM_DAY"
    else
        DAY="0$RANDOM_DAY"
    fi
    local DATETIME=$(date '+%H:%M:%S')
	
    local YEAR=2020

    mkdir $YEAR-$MON-$DAY\_$DATETIME
    touch -mad "$YEAR-$MON-$DAY $DATETIME" $YEAR-$MON-$DAY\_$DATETIME
}

for run in {1..10}
do
    mk
 # shuf -i 1-31 -n 1
done
