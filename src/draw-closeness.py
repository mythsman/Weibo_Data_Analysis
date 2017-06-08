import graph_tool as gt
import graph_tool.centrality
import numpy as np
import matplotlib.pyplot as plt

def work(num):
	g=gt.load_graph("../data/graph"+str(num)+".xml.gz")
		
	c=gt.centrality.closeness(g)

	fig=plt.figure()
	res=[]
	for i in c.a.tolist():
		if not str(i)=="nan":
			res.append(i)
	plt.hist(res,label="Closeness",bins=100)
	plt.legend(loc="upper right")
	plt.xlabel("Closeness")
	plt.ylabel("Count")
	fig.savefig('../pic/closeness'+str(num)+'.png')
	print 'max of closeness: '+str(np.max(res))
	print 'max of closeness: '+str(np.min(res))
	print 'mean of closeness: '+str(np.mean(res))
	print 'var of closeness: '+str(np.var(res))

if __name__=='__main__':
	work(500)
