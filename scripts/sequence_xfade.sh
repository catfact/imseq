#!/bin/bash


# almost, but weirdness at beginning
#ffmpeg -pattern_type glob -i 'test_frames/*.png' -vf zoompan=d=3.0:fps=2.0,framerate=25:interp_start=0:interp_end=255:scene=100 -c:v mpeg4 -maxrate 5M -q:v 2 test_xfade.mp4


# two-step version

# first, simple upsample: here it is 4 output frames per input stage
ffmpeg -framerate 0.5 -pattern_type glob -i 'test_frames/*.png' -r 2 -c:v libx264 -crf 25 temp.mp4
# next, apply framerate conversion. interpolation doesn't affect upsamplwed frames, only transitions
ffmpeg -i temp.mp4 -vf "framerate=fps=24" -codec:v mpeg4 test_xfade.mp4