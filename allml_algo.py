#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:33:03 2021

@author: devil
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
#%%
dir ='train'
categories = ['COVID','non-COVID']
data=[]
for category in categories:
    path =os.path.join(dir,category)
    label=categories.index(category)
    for img in os.listdir(path):
        imgpath =os.path.join(path,img)
        pet_img=cv2.imread(imgpath,0)
        try:
            pet_img=cv2.resize(pet_img,(100,100))
            image=np.array(pet_img).flatten()
        
            data.append([image,label])
        except Exception as e:
            pass
pick_in=open('data1.pickle','wb')
pickle.dump(data,pick_in)
pick_in.close()
#%%
pick_in=open('data1.pickle','rb')
data=pickle.load(pick_in)
pick_in.close()

random.shuffle(data)
features =[]
labels=[]

for feature,label in data:
    features.append(feature)
    labels.append(label)
xtrain,xtest,ytrain,ytest=train_test_split(features,labels,test_size=0.30)
#%%
model=SVC(C=1,kernel='poly',gamma='auto')
model.fit(xtrain,ytrain)
p=model.predict(xtest)

accuracy =model.score(xtest,ytest)
#%%
print('Accuracy is',accuracy)
#%%
print('prediction',p)

pic=xtest[0].reshape(100,100)
plt.imshow(pic,cmap='gray')
plt.show()
#%%
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(ytest,p)
#%%
from sklearn.neighbors import KNeighborsClassifier
classifier= KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
classifier.fit(xtrain,ytrain)
p=model.predict(xtest)
accuracy =classifier.score(xtest,ytest)
print(accuracy)
#%%
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy',random_state=0)
model.fit(xtrain,ytrain)
accuracy =model.score(xtest,ytest)
print(accuracy)