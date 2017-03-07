
import csv
import pickle
from pypinyin import pinyin, lazy_pinyin
import pypinyin

import glob

'''
Author : 高仲毅 backman.only@gmail.com	
2017/03/04
紀錄:
	當兵的血淚~~~




'''




def builAllDomainWordsDict(nameList):
	geoDict={}

	for name in nameList:

		with open(name+".txt",encoding = 'utf8') as f:
			for line in f.readlines():
				print (line )
				geoDict["-".join(lazy_pinyin(str(line[:-1])))]=str(line[:-1])

	pickle.dump(geoDict,open("./allPack/all.pack","wb"))
	



def buildDomainWordsDict(name):
	geoDict={}
	with open(name+".txt",encoding = 'utf8') as f:
		for line in f.readlines():
			print (line )
			geoDict["-".join(lazy_pinyin(str(line[:-1])))]=str(line[:-1])

	pickle.dump(geoDict,open("./team/"+name+".pack","wb"))
	


'''

for file in glob.glob("*.txt"):
	name=file.split(".")[0]
	print(name)
	buildDomainWordsDict(name)

wordList=[]
for file in glob.glob("*.txt"):
	name=file.split(".")[0]
	wordList.append(str(name))


builAllDomainWordsDict(wordList)
'''


buildDomainWordsDict("team")



