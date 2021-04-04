import json
from collections import defaultdict
import os 
import glob
import re
import cv2

category1 = ["data/bicycle/",0,2]
category2 = ["data/bus/",1,6]
category3 = ["data/car/",2,3]
category4 = ["data/motorcycle/",3,4]
category5 = ["data/truck/",4,8]

myCategories = [2,3,4,6,8]

myCat = {"data/bus/": 6,"data/car/": 3,'data/motorcycle':4,'data/truck':8}

def myannotations():
	print("Annotations Started")
	name_box_id = defaultdict(list)
	id_name = dict()
	
	f = open("annotations_trainval2017/instances_train2017.json",encoding='utf-8')
	data = json.load(f)
	myImages = []
	# print(data['images'])
	myImages = os.listdir(category1[0])
	myImages += os.listdir(category2[0])
	myImages += os.listdir(category3[0])
	myImages += os.listdir(category4[0])
	myImages += os.listdir(category5[0])


	myIds = []
	nameDict = {}
	for im in myImages:
		tStr = re.sub('\D','',im)
		# print("im", im, tStr)
		myIds.append(int(tStr))
		nameDict[ myIds[-1] ] = im

	# myIds = [int(im.split('.')[-2]) for im in myImages]
	# print("myIds",len(myIds))
	annotations = data['annotations']	
	
	
	for counter,ant in enumerate(annotations):
		try:

			idx = ant['image_id']
			cat = ant['category_id']
			myBB = []
			if cat in myCategories  and idx in myIds:
				filename = nameDict[idx]

				print("filename ",filename)

				if cat == category1[2]:
					myPath = category1[0]
					finalcat = category1[1]
				elif cat == category2[2]:
					myPath = category2[0]
					finalcat = category2[1]
				elif cat == category3[2]:
					myPath = category3[0]
					finalcat = category3[1]
				elif cat == category4[2]:
					myPath = category4[0]
					finalcat = category4[1]
				elif cat == category5[2]:
					myPath = category5[0]
					finalcat = category5[1]
				
				myim = cv2.imread(myPath + filename)
				imh,imw = myim.shape[0:2]

				print("Total bbs",ant['bbox'])
				finalBB = []
				[mya,myb,myc,myd] = [(ant['bbox'][0] + (ant['bbox'][2]/2))/imw,(ant['bbox'][1] + (ant['bbox'][3]/2))/imh,(ant['bbox'][2]/imw), (ant['bbox'][3]/imh)]
				
				myBB.append([round(mya,6),round(myb,6),round(myc,6),round(myd,6)])
				
				print("filename ",filename)
				myFil = filename.split('.')[-2]
				
				with open( myPath + myFil +'.txt', 'a') as mynewfile:
					for eachBB in myBB: mynewfile.write(str(finalcat) + ' ' + str(eachBB)[1:-1].replace(",","") + '\n')

				
			
			print("Total Images are {},working on {} \n".format(len(myImages),counter))
		except Exception as ex:
			print("file not",str(ex))
			pass

	
def genTxt():
	print("Generating train.txt Started")
	
	name_box_id = defaultdict(list)
	id_name = dict()
	
	f = open("annotations_trainval2017/instances_train2017.json",encoding='utf-8')
	data = json.load(f)
	myImages = []
	# print(data['images'])
	myImages = os.listdir(category1[0])
	myImages += os.listdir(category2[0])
	myImages += os.listdir(category3[0])
	myImages += os.listdir(category4[0])
	myImages += os.listdir(category5[0])


	myIds = []
	nameDict = {}
	for im in myImages:
		tStr = re.sub('\D','',im)
		# print("im", im, tStr)
		myIds.append(int(tStr))
		nameDict[ myIds[-1] ] = im

	# myIds = [int(im.split('.')[-2]) for im in myImages]
	# print("myIds",len(myIds))
	annotations = data['annotations']	
	busList = []
	trainFile = open("train.txt","a")
	for counter,ant in enumerate(annotations):
		idx = ant['image_id']
		cat = ant['category_id']
		myBB = []
		if cat in myCategories  and idx in myIds and not idx in busList:
			filename = nameDict[idx]
			print("filename ",filename)
			if cat == category1[2]:
				myPath = category1[0]
				finalcat = category1[1]
			elif cat == category2[2]:
				myPath = category2[0]
				finalcat = category2[1]
			elif cat == category3[2]:
				myPath = category3[0]
				finalcat = category3[1]
			elif cat == category4[2]:
				myPath = category4[0]
				finalcat = category4[1]
			elif cat == category5[2]:
				myPath = category5[0]
				finalcat = category5[1]
			
			busList.append(idx)
			
			trainFile.write(myPath + filename + '\n')

def mayannotations2():
	print("Annotations Started")
	name_box_id = defaultdict(list)
	id_name = dict()
	
	f = open("annotations_trainval2017/instances_train2017.json",encoding='utf-8')
	data = json.load(f)
	myImages = []
	# print(data['images'])
	myImages = os.listdir(category1[0])
	myImages += os.listdir(category2[0])
	myImages += os.listdir(category3[0])
	myImages += os.listdir(category4[0])
	myImages += os.listdir(category5[0])


	myIds = []
	nameDict = {}
	for im in myImages:
		tStr = re.sub('\D','',im)
		# print("im", im, tStr)
		myIds.append(int(tStr))
		nameDict[ myIds[-1] ] = im

	# myIds = [int(im.split('.')[-2]) for im in myImages]
	# print("myIds",len(myIds))
	annotations = data['annotations']	
	
	
	for counter,ant in enumerate(annotations):

		idx = ant['image_id']
		cat = ant['category_id']
		myBB = []
		if cat in myCategories  and idx in myIds:
			filename = nameDict[idx]

			print("filename ",filename)

			if cat == category1[2]:
				myPath = category1[0]
				finalcat = category1[1]
			elif cat == category2[2]:
				myPath = category2[0]
				finalcat = category2[1]
			elif cat == category3[2]:
				myPath = category3[0]
				finalcat = category3[1]
			elif cat == category4[2]:
				myPath = category4[0]
				finalcat = category4[1]
			elif cat == category5[2]:
				myPath = category5[0]
				finalcat = category5[1]
			print("Type bbs",type(ant['bbox']))
			print("Total bbs",ant['bbox'].split[','])
	
			myBB.append(ant['bbox'])
			
			print("filename ",filename)
			myFil = filename.split('.')[-2]
			
			with open( myPath + myFil +'.txt', 'a') as mynewfile:
				for eachBB in myBB: mynewfile.write(str(finalcat) + ' ' + str(eachBB)[1:-1] + '\n')

			
		
		print("Total Images are {},working on {} \n".format(len(myImages),counter))




def DataCleaning(mydir):
	try:
	
		TotalList = os.listdir(mydir)
		txtf = glob.glob("*.txt")
		imgfiles = glob.glob("*.jpg")
		txtIds  = [fn.split('.')[-2] for fn in txtf]
		imgfiles  = [In.split('.')[-2] for In in imgfiles]
		for eachFile in TotalList:
			thisFile = eachFile.split('.')[-2]
			if (thisFile not in txtIds) and (thisFile not in imgfiles):
				print("this file",thisFile)
				os.remove(mydir + thisFile + ".txt" )






	except Exception as ex:
		print("error in DataCleaning",str(ex))
		pass



	



myannotations()
# mayannotations2()
# DataCleaning(mydir = "/home/nitish/Master/MachineLearning/data/car/")
# genTxt()