
import csv
import pickle
from pypinyin import pinyin, lazy_pinyin
import pypinyin

'''
Author : 高仲毅 backman.only@gmail.com	
2017/03/04
紀錄:
    當兵的血淚~~~




'''

def buildDomainWordsDict():
	geoDict={}
	with open("斗南.txt",encoding = 'utf8') as f:
		for line in f.readlines():
			print (line )
			geoDict["-".join(lazy_pinyin(str(line[:-1])))]=str(line[:-1])

	pickle.dump(geoDict,open("geo_WG_Dict.pack","wb"))
	



buildDomainWordsDict()



