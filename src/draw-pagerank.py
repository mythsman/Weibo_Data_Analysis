import graph_tool as gt
import graph_tool.centrality
import numpy as np
import matplotlib.pyplot as plt

def work(num):
	g=gt.load_graph("../data/graph"+str(num)+".xml.gz")
	pr=gt.centrality.pagerank(g)

	fig=plt.figure()
	plt.hist(np.log10(pr.a),label="PageRank",bins=100)
	plt.legend(loc="upper right")
	plt.xlabel("PageRank")
	plt.ylabel("Count")
	fig.savefig('../pic/pagerank'+str(num)+'.png')

if __name__=='__main__':
	work(500)
