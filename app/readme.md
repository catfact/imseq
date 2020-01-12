# image_sequencer

a quick little utility to sequence bitmap images into videos. 
can perform some light procssing on input: 
- crop each frame
- replace arbitrary colors in each frame
- dissolve between each adjacent frame with arbitrary duration

assumptions:
- input files are named in sequence; zero-padding is not significant. (`1.png`, `02.png`, &c.)
- input files are RGB bitmaps 

single argument is a configation file. see `default_config.json` for the format.
all configuration fields are mandatory.

requires imagemagick to be installed:

linux:
```
sudo apt install imagemagick
```

macos:
```
brew install imagemagick
```

windows (??):
```
choco install imagemagick
```