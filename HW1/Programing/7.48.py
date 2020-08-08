import numpy as np

def mapping(x):  ######### Function to map generated symbols to the respective random vectors ( 0 -> (0,0),1 -> (0,1),2 -> (1,0),3 -> (1,1),)
	res = []
	for i in range(0,x.shape[0]):
		if(x[i]==0):
			res.append((0,0))
		if(x[i]==1):
			res.append((0,1))
		if(x[i]==2):
			res.append((1,0))
		if(x[i]==3):
			res.append((1,1))
	res = np.array(res)
	return res

def jointpmf(x): ######### Function to find Joint PMF
	res = np.zeros([2,2])
	for i in range(0,x.shape[0]):
		if(x[i][0]==0 and x[i][1]==0):
			res[0][0]+=1
		if(x[i][0]==0 and x[i][1]==1):
			res[0][1]+=1
		if(x[i][0]==1 and x[i][1]==0):
			res[1][0]+=1
		if(x[i][0]==1 and x[i][1]==1):
			res[1][1]+=1
	res = res*1.0/x.shape[0]
	print("Joint PMF from generated data is as follows")
	print(res)

def marginalpmf(x): ######### Function to find Marginal PMF
	res1 = np.zeros(2)
	res2 = np.zeros(2)
	for i in range(0,x.shape[0]):
		if(x[i][0]==0):
			res1[0]+=1
		if(x[i][0]==1):
			res1[1]+=1
	for i in range(0,x.shape[0]):
		if(x[i][1]==0):
			res2[0]+=1
		if(x[i][1]==1):
			res2[1]+=1
	res1 = res1/x.shape[0]
	res2 = res2/x.shape[0]
	print("Marginal PMF of X is")
	print(res1)
	print("Marginal PMF of Y is")
	print(res2)

nos = 100000 

choice = np.random.choice((0,1,2,3),size = nos, p = (0.125,0.125,0.25,0.5))
dist = mapping(choice)

jointpmf(dist)  ###### Estimated values of joint PMF
marginalpmf(dist)   ########### Estimated values of marginal PMF