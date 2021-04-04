# import cv2
import json
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import os
import sys
import glob
# with open("train.txt",'r') as f:
#     myl=f.readlines()


# for each in myl:
#     myName = each.split(' ')[0]
#     secondNamwe = each.split(' ')[1]
#     thiirdName = secondNamwe.split(',')
#     print("filename ",myName)
#     img = np.array(Image.open(myName), dtype=np.uint8)
#     fig,ax = plt.subplots(1)
#     ax.imshow(img)
#     xm = int(thiirdName[0])
#     ym = int(thiirdName[1])
#     w =  int(thiirdName[2])
#     h = int(thiirdName[3])
#     print("xm,ym,w,h",xm,ym,w,h)
#     rect = patches.Rectangle((xm,ym),(w - xm) ,(h-ym),linewidth=1,edgecolor='r',facecolor='none')
#     ax.add_patch(rect)
#     plt.show()
###000000401980,
# a,b,c,d = 52.36, 387.77, 176.36, 157.62
# a,b,c,d = 217.6, 463.62, 235.94, 75.8
# myx,myy = a + (c/2) , b + (d/2) 



# ####bicycle 74

# a,b,c,d = 2.75, 3.66, 159.4, 312.4
# myx,myy = a + (c/2) , b + (d/2)

def testimg(filename = "darknet/custom_data/images/car/000000000071.jpg"):
    try:
        img = np.array(Image.open(filename), dtype=np.uint8)
        print("shape",img.shape[0:2])
        imgH,imgw = img.shape[0:2]
        mytxtfile = (filename.split('/')[-1]).split('.')[-2] + '.txt'
        mytxtfilePath = "darknet/custom_data/labels/car/"
        file1 = open(mytxtfilePath + mytxtfile, 'r') 
        Lines = file1.readlines()
        myd = {}
        fig,ax = plt.subplots(1)
        ax.imshow(img)
        for counter,line in enumerate(Lines):
            line = line.strip('\n')
            mun = line.split(' ')
            # print("my num",mun)    
            leftx = float(mun[1].split(' ')[0]) - ((float(mun[3].split(' ')[0])/2)) 
            lefty = float(mun[2].split(' ')[0]) - (float(mun[4])/2) 
            leftx = leftx * imgw 
            # print("lefty",lefty)
            lefty = lefty * imgH
            bw = (float(mun[3].split(' ')[0])) * imgw
            bh = (float(mun[4].split(' ')[0])) * imgH
            myd[counter] = [leftx,lefty,bw,bh]
            
            for b in range(len(myd)):
                leftx,lefty,bw,bh = myd[b] 
                rect = patches.Rectangle((leftx,lefty),bw,bh,linewidth=1,edgecolor='r',facecolor='none')
                ax.add_patch(rect)
        # print("dict",myd)

        plt.show()

    except Exception as ex:
            # print("file not",str(ex))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno,exc_obj)
            print('Error :-', str(ex))


#4069 # 407225

# def Mytestimg(filename = "data/bicycle/000000000074.jpg",xm = a, ym =b, w = c, h = d):
#     img = np.array(Image.open(filename), dtype=np.uint8)
#     print("shape",img.shape[0:2])
#     imgH,imgw = img.shape[0:2]
#     fig,ax = plt.subplots(1)
#     ax.imshow(img)
#     print("centerx,centery",myx,myy)
#     ax.plot(myx,myy,'go',markersize=10)
#     leftx11 = myx - (w/2)
#     lefty11 = myy - (h/2)
#     print("lmax,lmin",leftx11,lefty11)

#     # ax.legend()
#     rect = patches.Rectangle((xm,ym),w,h,linewidth=1,edgecolor='r',facecolor='none')
#     ax.add_patch(rect)
#     plt.show()





def myAnnotations(myId = 74 ,myCat = 2):
    f = open("annotations_trainval2017/instances_train2017.json",encoding='utf-8')
    data = json.load(f)
    
    annotations = data['annotations']
    idx = myId
    cat = myCat
    myBB = []
    
    for ants in annotations:
        # print("my c",counter)

        if(ants['image_id'] == myId) and (ants['category_id'] == myCat):
            # print("my Data",len(ants))
            # print("my c",counter + 1)
            print("my Data",ants['bbox'])
            myBB.append(ants['bbox'])
            print("list of bbs",myBB)
            for eachBB in myBB:
                print("Look",str(eachBB)[1:-1])

            
    
def removeTxts(myLists = ["data/bicycle/","data/bus/","data/car/","data/motorcycle/","data/truck/"]):
    try:
        for directory in myLists:
            print("working on ",directory ) 
            mytxtf = glob.glob(directory + "*.txt")
            print("total images in directory is",len(mytxtf)) 
            for eachone in mytxtf:
                os.remove(eachone)
    except Exception as ex:
        print("Error in removeTxts",str(ex))

def myfunc():
    try:

        mytxf = glob.glob("data/truck/*.txt")
        mi = glob.glob("data/truck/*.jpg")
        print("length of txt files",len(mytxf))
        print("length of images",len(mi))


    except Exception as ex:
        print("Error in my func",str(ex))
        
            



    




testimg()
# Mytestimg()
# myAnnotations()
# removeTxts()
# myfunc()