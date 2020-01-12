import os
import sys

#--- helpers; perform OS calls to imagemagick

def blend(a, b, x):
    """
    create a blend of two images
    :param a: input path A
    :param b: input path B
    :param x: blending coefficient in [0, 1]
    :return: True on success, False on failure
    """
    # TODO
    pass


def sequence(dst, src, rate):
    """
    compose individual frame images into
    :param dst: output path
    :param src: search pattern for input paths
    :param rate: frame rate in hz
    :return: True on success, False on failure
    """
    # TODO
    pass

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

def replace_color(src, dst, a, b):
    """
    replace all instances of one color with another
    :param src: input filename
    :param dst: output filename
    :param a: color to replace as RGB hex string
    :param b: color to replace with, as RGB hex string
    :return:
    """
    # TODO
    pass