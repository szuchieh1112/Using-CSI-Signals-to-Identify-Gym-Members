from scipy import signal
import scipy.io as sio 
import matplotlib.pyplot as plt 
import numpy as np 
import time
from numpy import ndarray

strpath = '/1/5_12/Data/windows/Fok/'
CSIpath = '/1/5_12/Data/windows/Fok/CSI/'
CSIjpgpath = '/1/5_12/Data/windows/Fok/CSIjpg/'	
CPLpath = '/1/5_12/Data/windows/Fok/CPL/'
CPLjpgpath = '/1/5_12/Data/windows/Fok/CPLjpg/'

strtime = time.mktime(time.strptime("2022-05-05 19:10:57","%Y-%m-%d %H:%M:%S"))
endtime = time.mktime(time.strptime("2022-05-05 20:00:00","%Y-%m-%d %H:%M:%S"))
nowtime = int (strtime)

matwindow = ndarray((100,30),float)
butwindow = ndarray((100,30),float)
while(nowtime <= int(endtime)):
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
			Dnum = 1
			for i in range(0,100,20):
				matwindow = np.roll(matwindow,-20,axis = 0)
				matwindow[80:100] = dbA[i:i+20]

				x = range(1,101,1)
				for j in range(len(matwindow[1])):
					plt.plot(x,matwindow[:,j])
				plt.xlim(1,100)
				plt.ylim(10,35)
				plt.xlabel("time")
				plt.ylabel("CSI(DB)")

				endfn = CSIjpgpath+time.strftime("%m_%d(%H_%M_%S)",time.localtime(nowtime))+str(Dnum)+".jpg"
				plt.savefig(endfn)
				plt.close() 

				endfn = CSIpath+time.strftime("%m_%d(%H_%M_%S)",time.localtime(nowtime))+str(Dnum)+".mat"
				sio.savemat(endfn,{'dbA':matwindow})
				
				for j in range(len(matwindow[1])):
					b, a = signal.butter(6, 0.4, 'lowpass')   
					butdbA = signal.filtfilt(b, a, matwindow[:,j])  
					butwindow [:,j] = butdbA
					plt.plot(x,butdbA)
				plt.xlim(1,100)
				plt.ylim(10,35)
				plt.xlabel("time")
				plt.ylabel("CSI(DB)")
				endfn = CPLjpgpath+time.strftime("%m_%d(%H_%M_%S)",time.localtime(nowtime))+str(Dnum)+".jpg"
				plt.savefig(endfn)
				plt.close()

				endfn = CPLpath+time.strftime("%m_%d(%H_%M_%S)",time.localtime(nowtime))+str(Dnum)+".mat"
				sio.savemat(endfn,{'dbA':matwindow})
				
				Dnum = Dnum+1


