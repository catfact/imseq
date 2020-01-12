#!/bin/bash

if [ $# -gt 0 ]; then
    OUTPUT=$1
else
    OUTPUT="output.mp4"
fi

if [ $# -gt 1 ]; then
    PATTERN=$2
else
    $PATTERN="%d.png"
fi
if [ $# -gt 3 ]; then
    RATE=$3
else
    RATE=10
fi

# if [ $# -gt 4 ]; then
#     START=$4
# else
#     START=0
# fi


echo "output is $OUTPUT"
echo "pattern is $PATTERN"
echo "rate is $RATE"
#echo "start is $START"

#ffmpeg -i $PATTERN -start_number $START -r $RATE -s 1920x1080  -vcodec libx264 -crf 25 -vf fps=24 -pix_fmt yuv420p $OUTPUT
ffmpeg -pattern_type glob -i $PATTERN -r $RATE -s 1920x1080  -vcodec libx264 -crf 25 -vf fps=24 -pix_fmt yuv420p $OUTPUT