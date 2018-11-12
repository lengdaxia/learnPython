# -*- coding:utf-8 -*-

from PIL import Image

im = Image.open('python_captcha/captcha.gif')

# 将图片转换成 8位像素模式
im.convert("P")

print(im.histogram())

