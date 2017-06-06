#coding=utf-8
import matplotlib
from graph_tool.all import *

def saveAllGraph():
	g=Graph()

	fuser=open('../data/user.txt','r')
	uidDict={}
	cnt=0
	cntx=0
	for line in fuser:
		cnt+=1
		ids=line.split('\t')
		if uidDict.has_key(ids[0]):
			continue
		uidDict[ids[0]]=cntx
		cntx+=1

	g.add_vertex(cntx)
	fuser.close()
	print str(cntx)+' in '+str(cnt)+' users have been loaded.'

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
	g.save("../data/graphAll.xml.gz")
	
if __name__=='__main__':
	saveAllGraph()
