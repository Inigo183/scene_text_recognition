
import cv2
import numpy as np
import argparse

#Gestion de parametros
parser = argparse. ArgumentParser(description = 'Deteccion de texto con MSER')
parser.add_argument('--imagen','-i',type=str)
args = parser.parse_args()

#Create MSER object
mser = cv2.MSER_create()

#Your image path i-e receipt path 
img = cv2.imread(args.imagen)

#Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

vis = img.copy()

#detect regions in gray scale image
regions, _ = mser.detectRegions(gray)

hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]

cv2.polylines(vis, hulls, 1, (0, 255, 0))

cv2.imshow('mser', vis)

cv2.waitKey(0)

