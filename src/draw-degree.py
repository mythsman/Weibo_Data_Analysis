import graph_tool as gt
import matplotlib.pyplot as plt

g=gt.load_graph("../data/graphAll.xml.gz")

indegree_list=gt.stats.vertex_hist(g,"in")[0]
outdegree_list=gt.stats.vertex_hist(g,"out")[0]

fig=plt.figure()
plt.plot(indegree_list,label="Indegree distribution")
plt.plot(outdegree_list,label="Outdegree distribution")
plt.xlim(0,500)
plt.ylim(0,1000)
plt.legend(loc="upper right")
plt.xlabel("Degree")
plt.ylabel("Count")
fig.savefig("../pic/degree.png")
