import graph_tool as gt
import graph_tool.stats
import matplotlib.pyplot as plt
import numpy as np

def work(num):
	g=gt.load_graph("../data/graph"+str(num)+".xml.gz")

	indegree_list=gt.stats.vertex_hist(g,"in")[0]
	outdegree_list=gt.stats.vertex_hist(g,"out")[0]

	fig=plt.figure()
	plt.plot(indegree_list,label="Indegree distribution")
	plt.plot(outdegree_list,label="Outdegree distribution")
	plt.xlim(0,40)
	plt.ylim(0,100)
	plt.legend(loc="upper right")
	plt.xlabel("Degree")
	plt.ylabel("Count")
	fig.savefig("../pic/degree"+str(num)+".png")

	print 'max of indegree : '+str(np.max(indegree_list))
	print 'mean of indegree : '+str(np.mean(indegree_list))
	print 'variance of indegree : '+str(np.var(indegree_list))

	print 'max of outdegree : '+str(np.max(outdegree_list))
	print 'mean of outdegree : '+str(np.mean(outdegree_list))
	print 'variance of outdegree : '+str(np.var(outdegree_list))
if __name__=='__main__':
	work(500)

