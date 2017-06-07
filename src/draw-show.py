import graph_tool as gt
import graph_tool.draw
import numpy as np
import matplotlib.pyplot as plt

def work(num):
	g=gt.load_graph("../data/graph"+str(num)+".xml.gz")

	pos = gt.draw.sfdp_layout(g)
	gt.draw.graph_draw(g, pos=pos, output="../pic/sfdp_layout"+str(num)+".pdf")
	gt.draw.graph_draw(g, pos=pos, output="../pic/sfdp_layout"+str(num)+".png")

	pos = gt.draw.arf_layout(g, max_iter=0)
	gt.draw.graph_draw(g, pos=pos, output="../pic/arf_layout"+str(num)+".pdf")
	gt.draw.graph_draw(g, pos=pos, output="../pic/arf_layout"+str(num)+".png")
	
	pos = gt.draw.radial_tree_layout(g, g.vertex(0))
	gt.draw.graph_draw(g, pos=pos, output="../pic/radial_tree_layout"+str(num)+".pdf")
	gt.draw.graph_draw(g, pos=pos, output="../pic/radial_tree_layout"+str(num)+".png")

if __name__=='__main__':
    work(500)
