#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:54:51 2020

@author: nitish
"""

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os
import requests


pylab.rcParams['figure.figsize'] = (8.0, 10.0)
dataDir='./annotations_trainval2017'
dataType='val2017'
annFile='{}/instances_train2017.json'.format(dataDir)
coco=COCO(annFile)
mylist = ['car','motorcycle','bus','truck','bicycle'] 
catIds = coco.getCatIds(catNms=[mylist[0]])
imgIds = coco.getImgIds(catIds=catIds)
# annIds = coco.getAnnIds(imgIds=imgIds, catIds=catIds)

images = coco.loadImgs(imgIds)
myoriP = 'data/' + mylist[0] + '/'  
print("Total Images are ",len(images))
for counter,im in enumerate(images):
    print('Total images are {} , working on{}'.format(len(images),counter))
    img_data = requests.get(im['coco_url']).content
    with open(myoriP + im['file_name'], 'wb') as handler:
        handler.write(img_data)
    
    myId,mycat = im['id'],3
    annIds = coco.getAnnIds(imgIds=[myId], catIds=[mycat])
    anns = coco.loadAnns(annIds)
    myBob = []
    for i in range(len(anns)):
    	eb = anns[i]['bbox']
    	myBob.append(eb)

    with open(myoriP + im['file_name'].split('.')[-2] + '.txt', 'a') as f:
    	finalcat = 2
    	for eachBB in myBob:
    		f.write(str(finalcat) + ' ' + str(eachBB)[1:-1] + '\n')











##########################################################
# annIds = coco.getAnnIds(imgIds=[531], catIds=[2])
# anns = coco.loadAnns(annIds)
# print("my anns",anns[0]['bbox'])

# print("My annoation Info",type(anns),len(anns))
# myBob = []
# for i in range(len(anns)):
# 	print(i)
# 	eb = anns[i]['bbox']
# 	myBob.append(eb)

# print("this is boubdinhg box",myBob)
#################################################################