import sys
from helpers import *

#----------------
#--- app logic

print(sys.argv)

# make a copy of the source frames to temp folder

# crop each source frame in place

# for each color replacement rule, process each frame in place
replace_color("test_frames/22.png", "22_black.png", "#ffffff", "#000000", 0)

# perform sequencing
# sequence(None, None, None)

# clean up temp folder