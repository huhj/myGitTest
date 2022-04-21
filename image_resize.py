#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<更改图片尺寸>

import os
import os.path
from PIL import Image
import cv2
import matplotlib.pyplot as plt
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS)
  #resize image with high-quality
  out.save(fileout, type)
if __name__ == "__main__":
  #filein = '/home/li-lab/PycharmProjects/Resize/10845.jpg'
  imgfile = '/home/li-lab/PycharmProjects/Resize/input.jpg'
  #fileout = '/home/li-lab/PycharmProjects/Resize/10845sm.png'
  #width = 700
  #height = 710
  #type = 'png'
  #ResizeImage(filein, fileout, width, height, type)
  img = cv2.imread("/home/li-lab/PycharmProjects/Resize/Input.jpg")
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  plt.imshow(gray_img)
  plt.show()
