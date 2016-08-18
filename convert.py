# -*- coding: utf-8 -*-
__author__ = 'baijieying'
import re

rlist=[]
with open('d:\\shudian_testfile.txt','r') as f:
	for s in f.readlines():
		rlist.append(s)
print(len(rlist))
with open('shudian.template','r',encoding='utf-8') as ft:
	html = ft.read()
datainfo=''
datainfo+='''var data_info = ['''
for i in range(0,len(rlist),3):
	try:
		datainfo+='{{ name:{1},{0},{2}}},\n'.format(re.sub(r'["{}\n]','',rlist[i]),re.sub('\n','',rlist[i+1]),re.sub(r'["{}\n]','',rlist[i+2]))
	finally:
		print(i)
datainfo+='];'

newhtml=html.replace('mydata_info',datainfo)
with open('newshudian.html','w',encoding='utf-8') as fw:
	fw.write(newhtml)