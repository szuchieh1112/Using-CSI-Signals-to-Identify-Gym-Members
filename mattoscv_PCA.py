# coding=utf-8
import scipy.io as sio 
import matplotlib.pyplot as plt 
import numpy as np 
import cv2
import time
import csv

import matplotlib.pyplot as plt 
import sklearn
print (sklearn.__version__)
from sklearn.datasets import load_iris 
from sklearn.decomposition import PCA , IncrementalPCA
from itertools import chain
rrlstr = 'row'

fokpath = 'E:\\1\\5_12\\Data\\windows\\Fok\\CSI\\'
jiepath = 'E:\\1\\5_12\\Data\\windows\\Jie\\CSI\\'

with open('output.csv', 'w') as csvfile:
	writer = csv.writer(csvfile) 

	# 寫入第一列的欄位名稱
	stroutscv = []
	pintstr = ['A','B','C']
	for l in range(1):
		for j in range(1):
			for k in range(30):
				stroutscv.append(pintstr[l] + str(j) +str(k))
	stroutscv.append('label')
	writer.writerow(stroutscv)
	#數據處理與輸出
	for i in range(1,200,1):
		matname = str(i)+'.mat'
		matfn = fokpath + matname
		try:
			data=sio.loadmat(matfn) 
		except IOError:
			print ("no data\n")
		else:
			plt.close('all') 
			dbA=data['dbA'] 
			dbB=data['dbB'] 
			dbC=data['dbC'] 
			sumA = []
			sumB = []
			sumC = []
			lab = 0
			print (i)
			for j in range(30):
				wave_dataA = []
				wave_dataB = []
				wave_dataC = []
				wave_dataA.append(dbA[:,j]) 
				wave_dataA.append(dbB[:,j]) 
				wave_dataA.append(dbC[:,j]) 
				#轉相位
				pca = PCA(n_components=1)
				dataA1 = pca.fit(wave_dataA).transform(wave_dataA)
				dataA2 = abs(dataA1)
				sumA.append(dataA2[0])
			outscv = sumA
			outscv = list(chain.from_iterable(outscv))
			outscv.append(lab)
			# print (outscv)
			writer.writerow(outscv)
		finally:
			pass
	print ("fokpath OK\n")
	'''
	for i in range(1,200,1):
		matname = str(i)+'.mat'
		matfn = jiepath + matname
		try:
			data=sio.loadmat(matfn) 
		except IOError:
			print ("no data\n")
		else:
			plt.close('all') 
			dbA=data['dbA'] 
			dbB=data['dbB'] 
			dbC=data['dbC'] 
			sumA = []
			sumB = []
			sumC = []
			lab = 1
			print (i)
			for j in range(30):
				wave_dataA = []
				wave_dataA.append(dbA[:,j]) 
				wave_dataA.append(dbB[:,j]) 
				wave_dataA.append(dbC[:,j]) 
				#PCA
				wave_dataA = list(wave_dataA)
				pca = PCA(n_components=1)
				dataA1 = pca.fit(wave_dataA).transform(wave_dataA)
				dataA2 = abs(dataA1)
				sumA.append(dataA2[0])
			outscv = sumA
			outscv = list(chain.from_iterable(outscv))
			outscv.append(lab)
			writer.writerow(outscv)
		finally:
			pass
	print ("jiepath OK\n")