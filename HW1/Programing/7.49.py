import numpy as np

def mapping(x): ######### Function to map generated symbols to the respective random vectors ( 0 -> (0,0),1 -> (0,1),2 -> (1,0),3 -> (1,1),)
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

nos = 100000

choice = np.random.choice((0,1,2,3),size = nos, p = (0.125,0.125,0.25,0.5))
dist = mapping(choice)

M = dist.shape[0]

x_bar = np.sum(dist[:,0])/M
y_bar = np.sum(dist[:,1])/M
# print(x_bar,y_bar)
xmym = 0
xm2 = 0
ym2 = 0
for i in range(0,dist.shape[0]):
	xmym+=dist[i,0]*dist[i,1]
	xm2+=dist[i,0]*dist[i,0]
	ym2+=dist[i,1]*dist[i,1] 

xmym = xmym/M
xm2 = xm2/M
ym2 = ym2/M

rho = (xmym-x_bar*y_bar)/np.sqrt((xm2-x_bar*x_bar)*(ym2-y_bar*y_bar))
print("The corrrelation coefficient is ")
print(rho)