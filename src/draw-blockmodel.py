import graph_tool as gt
import graph_tool.inference
import graph_tool.centrality
import numpy as np
import matplotlib.pyplot as plt

def work(num):
	g=gt.load_graph("../data/graph"+str(num)+".xml.gz")
	state = gt.inference.minimize_blockmodel_dl(g)
	deg = g.degree_property_map("in")
	deg.a = 4 * (np.sqrt(deg.a) * 0.5 + 0.4)
	ebet = gt.centrality.betweenness(g)[1]
	ebet.a /= ebet.a.max() / 10.
	eorder = ebet.copy()
	eorder.a *= -1
	state.draw(vertex_shape=state.get_blocks(),output="../pic/blockmodel"+str(num)+".pdf",vertex_size=deg, vertex_fill_color=deg, vorder=deg,edge_color=ebet, eorder=eorder, edge_pen_width=ebet)
	state.draw(vertex_shape=state.get_blocks(),output="../pic/blockmodel"+str(num)+".png",vertex_size=deg, vertex_fill_color=deg, vorder=deg,edge_color=ebet, eorder=eorder, edge_pen_width=ebet)

if __name__=='__main__':
    work(500)
