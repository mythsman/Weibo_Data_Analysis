import graph_tool as gt
import graph_tool.inference
import graph_tool.centrality
import numpy as np
import matplotlib.pyplot as plt

def work(num):
	g=gt.load_graph("../data/graph"+str(num)+".xml.gz")
	state = gt.inference.minimize_nested_blockmodel_dl(g)
	state.draw(output="../pic/nestedblockmodel"+str(num)+".pdf")
	state.draw(output="../pic/nestedblockmodel"+str(num)+".png")

if __name__=='__main__':
    work(500)
