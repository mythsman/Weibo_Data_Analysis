## 原始数据
### user.txt
64452条用户信息，包括：
用户编号，用户编号2(暂时不用)，昵称，性别，个性签名
以制表符分割
例:
```
1000005991	1005051000005991	衷柏夷	他	活在当下,且行且珍惜	福建
1000124571	1005051000124571	工信布	他	互联网科技、经济、生活与宽窄新锐哲思。出版有《互联网时代的浪漫与痛痒——传统行业转型之道》、《嬗变》、《宏声传播集》等。	四川
1000241231	1005051000241231	翡翠羽裳	她	发现近在咫尺的美广东
1000463683	1005051000463683	Ann宝贝琴	她	有一种爱，是信念，从未向时间屈服。	江苏
1000585644	1005051000585644	知心老王	他	心情好，才是真的好！	北京
1000655734	1005051000655734	苏伊finjamie	他		江苏
1000726952	1005051000726952	张毅伟yy	他	上海交通大学EMBA校友会副主席领导力及企业策划专家致力于德鲁克管理的传播	上海
1000830690	1005051000830690	-金浩翔	他		浙江
1000891302	1005051000891302	杨越VJ	他	SMG魅力音乐电视频道总监，VJ，有事电邮yangyue3003@hotmail.com	上海
1001121254	1005051001121254	Rainboy2018	他		北京
```

### star.txt
6339630条点赞关系，包括：
点赞用户编号，被点赞用户编号，点赞时间
以制表符分割，时间格式为YYYY-MM-DD HH:MM:SS
例:
```
1000005991	1065618283	2016-07-12 17:16:47
1000005991	1067942913	2015-09-06 21:35:39
1000005991	1101519144	2014-08-30 23:14:13
1000005991	1180514263	2015-06-11 15:05:19
1000005991	1187900115	2014-06-12 19:14:10
1000005991	1189590121	2015-08-28 23:46:37
1000005991	1191965271	2014-08-17 21:54:44
1000005991	1191965271	2016-02-16 11:13:35
1000005991	1195389671	2015-10-05 16:16:09
1000005991	1198367585	2015-09-23 23:43:51
```

### relatation.txt
34111736条关注关系，包括：
关注者，被关注者
以制表符分割
例:
```
1000005991	1004941280
1000005991	1005592945
1000005991	1007262567
1000005991	1007330514
1000005991	1008927295
1000005991	1008965464
1000005991	1009493500
1000005991	1057805991
1000005991	1062133183
1000005991	1067942913
```

## 构建模型
### 构建原始数据
```python
#coding=utf-8
import matplotlib
from graph_tool.all import *

def saveAllGraph():
    g=Graph()

    fuser=open('user.txt','r')
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

    fstar=open('star.txt','r')
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

    frelation=open('relation.txt','r')
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
    g.save("graphAll.xml.gz")

if __name__=='__main__':
    saveAllGraph()

```
user vertex:	64422
star edge:		2570280
relation edge:	9051246

### 删除入度为1的节点
```python

```
vertex:
edge:

