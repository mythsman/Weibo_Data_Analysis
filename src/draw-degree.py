import graph_tool as gt
import graph_tool.stats
import matplotlib.pyplot as plt

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

if __name__=='__main__':
	work(500)

