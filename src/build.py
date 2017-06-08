#coding=utf-8
import matplotlib
from graph_tool.all import *

def saveGraph(num=None):
	g=Graph()

	# Load user.txt
	fuser=open('../data/user.txt','r')
	uidDict={}
	cnt=0
	cntx=0
	for line in fuser:
		cnt+=1
		if cntx==num:
			continue
		ids=line.split('\t')
		if uidDict.has_key(ids[0]):
			continue
		uidDict[ids[0]]=cntx
		cntx+=1

	g.add_vertex(cntx)
	fuser.close()
	print str(cntx)+' in '+str(cnt)+' users have been loaded.'

	# Load star.txt
	fstar=open('../data/star.txt','r')
	cnt=0
	cntx=0
	for line in fstar:
		cnt+=1
		ids=line.split('\t')
		if uidDict.has_key(ids[0]) and uidDict.has_key(ids[1]) and not ids[0]==ids[1]:
			cntx+=1
			g.add_edge(uidDict[ids[0]],uidDict[ids[1]])
	print str(cntx)+' in '+str(cnt)+' stars have been loaded.'
	fstar.close()
	
	# Load relation.txt
	frelation=open('../data/relation.txt','r')
	cnt=0
	cntx=0
	for line in frelation:
		cnt+=1
		ids=line.split('\t')
		if uidDict.has_key(ids[0]) and uidDict.has_key(ids[1][:-1]):
			cntx+=1
			g.add_edge(uidDict[ids[0]],uidDict[ids[1][:-1]])
	print str(cntx)+' in '+str(cnt)+' relations have been loaded.'
	frelation.close()

	# Remove isolated vertex
	if num!=None:
		for v in reversed(sorted(g.vertices())):
			if v.in_degree()==0 and v.out_degree()==0:
				g.remove_vertex(v)
	
	print "Totally we have "+str(g.num_vertices())+" vertices and "+str(g.num_edges())+" edges";

	# Save data
	if num==None:
		g.save("../data/graphAll.xml.gz")
	else:
		g.save("../data/graph"+str(num)+".xml.gz")
		
	
if __name__=='__main__':
	saveGraph(500)
