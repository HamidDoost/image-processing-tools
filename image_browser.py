'''
===============================================================================
-- Author:		Hamid Doostmohammadi, Azadeh Nazemi
-- Create date: 01/11/2020
-- Description:	This code is a simple tool for showing images in the browser.
-- Status:      In progress
===============================================================================
'''


import imutils
from imutils import paths
import numpy as np
import cv2
import os
import sys
from imutils.paths import list_images

fileMode = "jpg"
fileout = open(sys.argv[1].split("\\")[-1]+".html", "w")

imagePaths = sorted(list(paths.list_images(sys.argv[1])))
L = "<!DOCTYPE html>\n"
fileout.writelines(L)

L = "<html>\n"
fileout.writelines(L)

L = "<body>\n"
fileout.writelines(L)

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    filename = imagePath.split("\\")[-1]
    part = cv2.resize(image, (600, 280))

    L = "<img src="+imagePath+"  alt=tray width=600 height=280>\n"
    fileout.writelines(L)


L = " <p id=demo></p>\n"
fileout.writelines(L)

L = "<script>"
fileout.writelines(L)

L = "function myFunction() }\n"
fileout.writelines(L)
