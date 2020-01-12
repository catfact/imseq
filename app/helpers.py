import os
import json

def parse_config(file):
    """
    parse a configuration JSON file
    :param file: path to .json
    :return: configuration as dictionary
    """
    with open(file) as json_file:
        data = json.load(json_file)
        print(data)
        return data

def sequence(dst, src, rate):
    """
    compose individual frame images into
    :param dst: output path
    :param src: search pattern for input paths (glob)
    :param rate: frame rate in hz
    :return: True on success, False on failure
    """
    print("sequencing frames to temp file...")
    cmd = 'ffmpeg -y -framerate 0.5 -pattern_type glob -i "{}" -r 2 -c:v libx264 -crf 0 temp.mp4'.format(src)
    os.system(cmd)
    print("done.")
    print("interpolating...")
    cmd = 'ffmpeg -y -i temp.mp4 -vf "framerate=fps=24" -codec:v mpeg4 test_{}'.format(dst)
    os.system(cmd)
    print("done.")


def crop(src, dst, x, y, w, h):
    """
    crop an image
    :param src: input path
    :param dst: output path
    :param x: offset from left edge in pixels
    :param y: offset from top edge in pixels
    :param w: width in pixels
    :param h: height in pixels
    :return: rue on success, False on failure
    """
    # TODO
    pass

def replace_color(src, dst, a, b, fuzz):
    """
    replace all instances of one color with another
    :param src: input filename
    :param dst: output filename
    :param a: color to replace as RGB hex string
    :param b: color to replace with, as RGB hex string
    :param fuzz: selection fuzz factor, as percentage
    :return:
    """
    cmd = 'convert {} -fuzz {}% -fill "{}" -opaque "{}" {}'.format(src, fuzz, b, a, dst)
    print(cmd)
    os.system(cmd)