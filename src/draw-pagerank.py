import graph_tool as gt
import graph_tool.centrality
import numpy as np
import matplotlib.pyplot as plt

def work(num=None):
	if num==None:
		g=gt.load_graph("../data/graphAll.xml.gz")
	else:
		g=gt.load_graph("../data/graph"+str(num)+".xml.gz")
		
	pr=gt.centrality.pagerank(g)

	fig=plt.figure()
	plt.hist(np.log10(pr.a),label="PageRank",bins=100)
	plt.legend(loc="upper right")
	plt.xlabel("PageRank")
	plt.ylabel("Count")
	if num==None:
		fig.savefig('../pic/pagerank.png')
	else:
		fig.savefig('../pic/pagerank'+str(num)+'.png')
	
	print 'max of pagerank: '+str(np.max(pr.a.tolist()))
	print 'min of pagerank: '+str(np.min(pr.a.tolist()))
	print 'mean of pagerank: '+str(np.mean(pr.a.tolist()))
	print 'variance of pagerank: '+str(np.var(pr.a.tolist()))

if __name__=='__main__':
	work(500)
