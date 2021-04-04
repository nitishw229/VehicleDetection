#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:43:10 2020

@author: nitish
"""

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os
import requests
import matplotlib.patches as patches

myId = 4
pylab.rcParams['figure.figsize'] = (8.0, 10.0)
dataDir='./annotations_trainval2017'
dataType='val2017'
annFile='{}/instances_train2017.json'.format(dataDir)
coco=COCO(annFile)
mylist = ['car','motorcycle','bus','truck','bicycle'] 
catIds = coco.getCatIds(catNms=[mylist[myId]])
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)
myoriP = 'data/' + mylist[myId] + '/'  
print("Total Images are ",len(images))
for im in images:
    img_data = requests.get(im['coco_url']).content
    with open(myoriP + im['file_name'], 'wb') as handler:
        handler.write(img_data)


imgPath = images = coco.loadImgs(anns[0]['id'])
tImg = io.imread(imgPath[0]['coco_url'])
bBox = anns[0]['bbox']

#tRect = patches.Rectangle((bBox[0] - bBox[2]/2, bBox[1] - bBox[3]/2), bBox[2], bBox[3], linewidth=10, fill=False)
tRect = patches.Rectangle((bBox[0], bBox[1]), bBox[2], bBox[3], linewidth=10, fill=False)

fig, ax = plt.subplots(1)
ax.imshow(tImg[:, :, :])
ax.add_patch(tRect)







