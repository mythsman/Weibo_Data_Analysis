import graph_tool as gt
import graph_tool.centrality
import numpy as np
import matplotlib.pyplot as plt

def work(num):
	g=gt.load_graph("../data/graph"+str(num)+".xml.gz")
		
	vp, ep=gt.centrality.betweenness(g)

	fig=plt.figure()
	res=plt.hist(vp.a,label="Betweenness of vertices",bins=100)
	plt.xlim(0,0.04)
	plt.ylim(0,250)
	plt.legend(loc="upper right")
	plt.xlabel("Betweenness")
	plt.ylabel("Count")
	fig.savefig('../pic/betweenness_vertices'+str(num)+'.png')
	print 'max of betweenness_vertices: '+str(np.max(res[1]))
	print 'mean of betweenness_vertices: '+str(np.mean(res[1]))
	print 'var of betweenness_vertices: '+str(np.var(res[1]))

	fig=plt.figure()
	res=plt.hist(ep.a,label="Betweenness of edges",bins=100)
	plt.xlim(0,0.015)
	plt.ylim(0,300)
	plt.legend(loc="upper right")
	plt.xlabel("Betweenness")
	plt.ylabel("Count")
	fig.savefig('../pic/betweenness_edges'+str(num)+'.png')
	print 'max of betweenness_edges: '+str(np.max(res[1]))
	print 'mean of betweenness_edges: '+str(np.mean(res[1]))
	print 'var of betweenness_edgees: '+str(np.var(res[1]))

if __name__=='__main__':
	work(500)
