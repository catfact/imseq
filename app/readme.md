# image_sequencer

a quick little utility to sequence bitmap images into videos. 
can perform some light processing on input: 
- crop each frame
- replace arbitrary colors in each frame
- dissolve between each adjacent frame with arbitrary duration

assumptions:
- input files are named in sequence; zero-padding is not significant. (`1.png`, `02.png`, &c.)
- input files are RGB bitmaps 
- single script argument is a configuration file. see `default_config.json` for the format.
all configuration fields are mandatory.

## requirements

python 3, imagemagick and ffmpeg

linux:
```
sudo apt install imagemagick ffmpeg python3
```

macos:
```
brew install imagemagick ffmpeg python
```
