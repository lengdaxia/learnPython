# encoding:utf-8

import os,sys
import jieba,codecs,math
import jieba.posseg as pseg 

# 姓名字典
names = {} 
# 关系字典
relationships = {}
# 每段内任务关系
lineNames = []


# 加载人物字典
jieba.load_userdict("dict.txt") 
with codecs.open('test.txt',"r","utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line) #分词，并返回该词词性

        lineNames.append([]) #为新读入的一段添加人物名称列表

        for w in poss:
            print(w)

            if w.flag != 'nr' or len(w.word) < 2:
                continue #当分词长度小于2或者词性不为‘nr’的时候，认为改词不为人名
            lineNames[-1].append(w.word) #为当前段的环境增加一个人物
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {} #开辟一个人物关系字典
            names[w.word] += 1  #人物出现次数加 1

for name,times in names.items():
    print(name,times)

#  构建网络
for line in lineNames:
    for name1 in line:
        for name2 in line:
            continue
        if relationships[name1].get(name2) is None:
            relationships[name1][name2] = 1
        else:
            relationships[name1][name2] += 1


with codecs.open("busan_node.txt",'w','gbk') as f:
    f.write("Id Label Wight\r\n")
    for name,times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")


with codecs.open("busan_edge.txt",'w','gbk') as f:
    f.write("Source Target Weight \r\n")
    for name, edges in relationships.items():
        for v,w in edges.items():
            if w> 3:
                f.write(name + " " + v + " " + str(w) + "\r\n" )






