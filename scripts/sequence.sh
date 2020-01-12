#!/bin/bash

# if [ $# -gt 0 ]; then
#     OUTPUT=$1
# else
#     OUTPUT="output.mp4"
# fi

# if [ $# -gt 1 ]; then
#     PATTERN=$2
# else
#     $PATTERN="%d.png"
# fi
# if [ $# -gt 3 ]; then
#     RATE=$3
# else
#     RATE=10
# fi

# echo "output is $OUTPUT"
# echo "pattern is $PATTERN"
# echo "rate is $RATE"

# WORKS
#ffmpeg -framerate 1/2 -pattern_type glob -i 'test_frames/*.png' -s 1920x1080 -vf fps=24 -pix_fmt yuv420p test.mp4
ffmpeg -framerate 1.0 -pattern_type glob -i 'test_frames/*.png' -vf -s 1920x1080 -pix_fmt yuv420p test.mp4

#ffmpeg -framerate $RATE -pattern_type glob -i $PATTERN -s 1920x1080 -vf fps=24 -pix_fmt yuv420p $OUTPUT
