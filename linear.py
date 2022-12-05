from scipy import signal
import scipy.io as sio 
import numpy as np 
import math
import time
from numpy import ndarray

strpath = '\1\5_12\Data\windows\Fok\'
endpath = '\1\5_12\Data\windows\Fok\Linear\'


for i in range(1,200,1):
		matname = str(i)+'.mat'
		matfn = strpath + matname
		try:
			data=sio.loadmat(matfn) 
		except IOError:
			print ("no data\n")
		else:
			dbA=data['dbA'] 	
			dbB=data['dbB']
			dbC=data['dbC']
			for j in range(20):
				for k in range(30):
					n0 = 0
					n1 = 0
					if(math.isinf(dbA[j][k])):
						n0 = k - 1
						while n0 > 0:
							if(math.isinf(dbA[j][n0])):
								n0 = n0 - 1
							else:
								break
						n1 = k + 1
						while(n1 <= 30):
							if(math.isinf(dbA[j][n1])):
								n1 = n1 + 1
							else:
								break
					if(n0 < 1):
						dbA[j][k] = dbA[j][n1]
					elif(n1 > 30):
						dbA[j][k] = dbA[j][n0]
					else:
						dbA[j][k] = dbA[j][n0] + (k - n0) * ((dbA[j][n1] - dbA[j][n0]) / (n1 - n0))



					n0 = 0
					n1 = 0
					if(math.isinf(dbB[j][k])):
						n0 = k - 1
						while(n0 > 0):
							if(math.isinf(dbB[j][n0])):
								n0 = n0 - 1
							else:
								break
						n1 = k + 1
						while(n1 <= 30):
							if(math.isinf(dbB[j][n1])):
								n1 = n1 + 1
							else:
								break
					if(n0 < 1):
						dbB[j][k] = dbB[j][n1]
					elif(n1 > 30):
						dbB[j][k] = dbB[j][n0]
					else:
						dbB[j][k] = dbB[j][n0] + (j - n0) * ((dbB[j][n1] - dbB[j][n0]) / (n1 - n0))



					n0 = 0
					n1 = 0
					if(math.isinf(dbC[j][k])):
						n0 = j - 1
						while(n0 > 0):
							if(math.isinf(dbC[j][n0])):
								n0 = n0 - 1
							else:
								break
						n1 = k + 1
						while(n1 <= 30):
							if(math.isinf(dbC[j][n1])):
								n1 = n1 + 1
							else:
								break
					if(n0 < 1):
						dbC[j][k] = dbC[j][n1]
					elif(n1 > 30):
						dbC[j][k] = dbC[j][n0]
					else:
						dbC[j][k] = dbC[j][n0] + (j - n0) * ((dbC[j][n1] - dbC[j][n0]) / (n1 - n0))

			endfn = endpath+str(i)+".mat"
			sio.savemat(endfn,{'dbA':dbA,'dbB':dbB,'dbC':dbC})