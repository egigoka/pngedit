#! python3
# -*- coding: utf-8 -*-
from commands7 import *  # mine commands
from PIL import Image


class State:
    image_input = "input2x2.png"
    image_output = "failname.png"
    json_file = "picsedit.json"


class JsonLocal:
    string = None
    json_file = State.json_file

    @classmethod
    def load(cls, filename=json_file):
        cls.string = Json.load(filename)

    @classmethod
    def save(cls, filename=json_file):
        Json.save(filename, cls.string)


JsonLocal.load()


class ImageCurrent:
    color_depth = 255
    width = None
    height = None
    pixels_list = []
    size = [width, height]

    @classmethod
    def update_output_filename(cls):
        State.image_output = "output" + str(cls.width) + "x" \
                             + str(cls.height) + ".png"
    @classmethod
    def update_size(cls):
        cls.size = [cls.width, cls.height]

    @classmethod
    def consist(cls):
        cls.update_output_filename()
        cls.update_size()

    @classmethod
    def set_width(cls, width):
        cls.width = width
        cls.consist()

    @classmethod
    def set_height(cls, height):
        cls.height = height
        cls.consist()

    @classmethod
    def create_random_pixels(cls):
        len_of_list = cls.width * cls.height
        cnt = 0
        cls.pixels_list = []
        while cnt< len_of_list:
            cnt += 1
            rand_r = Random.integer(0, cls.color_depth)
            rand_g = Random.integer(0, cls.color_depth)
            rand_b = Random.integer(0, cls.color_depth)
            rand_a = Random.integer(0, cls.color_depth)
            pixel_typle = (rand_r, rand_g, rand_b, rand_a)
            cls.pixels_list.append(pixel_typle)

    @classmethod
    def create_rainbow_pixels(cls):  # didn't work yet
        len_of_list = cls.width * cls.height
        cnt = 0
        cls.pixels_list = []
        rand_r =
        while cnt< len_of_list:
            cnt += 1
            if rand_r == 256:
                rand_r = 0
            else:
                rand_r += 1
            rand_r = Random.integer(0, cls.color_depth)
            rand_g = Random.integer(0, cls.color_depth)
            rand_b = Random.integer(0, cls.color_depth)
            rand_a = Random.integer(0, cls.color_depth)
            pixel_typle = (rand_r, rand_g, rand_b, rand_a)
            cls.pixels_list.append(pixel_typle)




ImageCurrent.set_width(100)
ImageCurrent.set_height(100)


image = Image.open(State.image_input)
debug_print("image.mode", image.mode, "image.size", image.size)
image_out = Image.new(image.mode,ImageCurrent.size)

pixels = list(image.getdata())
ImageCurrent.create_random_pixels()
ImageCurrent.create_rainbow_pixels()
pixels = ImageCurrent.pixels_list
debug_print("pixels", pixels)
#pixels.pop()
debug_print("pixels", pixels)
# cnt = 0
# for pixel in pixels:
#     cnt += 1
#     pixels_2
# pixels = []
# print(type([]))
# print(type(()))
cnt =0
# while cnt<255:
#     cnt += 1
#     pixels.append([(100,cnt,100,255)])
image_out.putdata(pixels)

image_out.save(State.image_output)
image_out.show()
