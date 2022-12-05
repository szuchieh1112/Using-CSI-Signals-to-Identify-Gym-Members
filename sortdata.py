import scipy.io as sio 
import matplotlib.pyplot as plt 
import numpy as np 
import cv2
import time


strpath = 'C:\\5_12\Data\windows\Fok'
endpathW = 'C:\\5_12\Data\windows\Fok\row'
endpathD = '/home/csi/CSI/CSITOOL/CSIdatainput/data/jie/right/'

Wnum = 1
Dnum = 1
akey = 119
strtime = time.mktime(time.strptime("2022-05-05 19:00:00","%Y-%m-%d %H:%M:%S"))
endtime = time.mktime(time.strptime("2022-05-05 20:00:00","%Y-%m-%d %H:%M:%S"))
nowtime = int (strtime)
#for nowtime in range(int(strtime),int(endtime),1):
while(nowtime <= int(endtime)):
	#imgname = time.strftime("%m-%d %H:%M:%S.jpg",time.localtime(nowtime))
	#frame = cv2.imread(strpath+imgname) 
	
	#if (type(frame) is np.ndarray) :
	#	cv2.imshow('frame', frame)
	#	akey = cv2.waitKey(0) & 0xFF
	#else:
	#	nowtime = nowtime+1
	
	#
	#if akey == ord('q'):
	#	nowtime = nowtime+1




	#
	if akey == ord('w'):
		matname = time.strftime("%m_%d(%H_%M_%S).mat",time.localtime(nowtime))
		matfn = strpath + matname
		nowtime = nowtime+1
		try:
			data=sio.loadmat(matfn) 
		except IOError:
			print ("no data\n")
		else:
			dbA=data['dbA'] 
			dbB=data['dbB'] 
			dbC=data['dbC']
			endfn = endpathW+str(Wnum)+".mat"   
			sio.savemat(endfn,{'dbA':dbA,'dbB':dbB,'dbC':dbC})
			Wnum=Wnum+1
		finally:
			pass
	# 
	if akey ==  ord('d'):
		matname = time.strftime("%m-%d %H:%M:%S.mat",time.localtime(nowtime))
		matfn = strpath + matname
		nowtime = nowtime+1
		try:
			data=sio.loadmat(matfn) 
		except IOError:
			print ("no data\n")
		else:
			dbA=data['dbA'] 
			dbB=data['dbB'] 
			dbC=data['dbC']
			endfn = endpathD+str(Dnum)+".mat"   
			sio.savemat(endfn,{'dbA':dbA,'dbB':dbB,'dbC':dbC})
			Dnum=Dnum+1
		finally:
			pass
	