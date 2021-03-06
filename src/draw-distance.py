import graph_tool as gt
import graph_tool.stats
import numpy as np
import matplotlib.pyplot as plt

def work(num=None):
	if num==None:
		g=gt.load_graph("../data/graphAll.xml.gz")
	else:
		g=gt.load_graph("../data/graph"+str(num)+".xml.gz")
		
	res=gt.stats.distance_histogram(g)	#May cost much time.

	fig=plt.figure()
	plt.plot(res[0],label="Distance distribution")
	plt.legend(loc="upper right")
	plt.xlabel("Distance")
	plt.ylabel("Count")
	if num==None:
		fig.savefig("../pic/distance.png")
	else:
		fig.savefig("../pic/distance"+str(num)+".png")

	fig=plt.figure()
	res[0][0]=1
	plt.plot(np.log10(res[0]),label="Log-distance distribution")
	plt.legend(loc="upper right")
	plt.xlabel("Distance")
	plt.ylabel("Log-count")
	
	if num==None:
		fig.savefig("../pic/log-distance.png")
	else:
		fig.savefig("../pic/log-distance"+str(num)+".png")

	max_distance=max(res[1])-1
	avg_distance=np.sum(res[0]*res[1][:-1])/np.sum(res[0])
	print 'max_distance: '+str(max_distance)
	print 'avg_distance: '+str(avg_distance)

if __name__=='__main__':
	work(500)
