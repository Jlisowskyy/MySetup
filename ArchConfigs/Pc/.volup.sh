#!/bin/sh

MAXVOL=125
STEP=5
ACTVOL=`pactl get-sink-volume @DEFAULT_SINK@ | awk -F '/' '{print $2}' | grep -o '[0-9]\+'`

# Check to no raise volume above MAXVOL barrier
if [ $ACTVOL -lt $MAXVOL ]; then
    pactl set-sink-volume @DEFAULT_SINK@ "+${STEP}%"
fi