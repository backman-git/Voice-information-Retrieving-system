
import csv
import pickle
from pypinyin import pinyin, lazy_pinyin
import pypinyin



def buildDomainWordsDict():
	geoDict={}
	with open("yulin.txt","r") as f:
		for line in f.readlines():
			geoDict["-".join(lazy_pinyin(str(line[:-1])))]=str(line[:-1])

	pickle.dump(geoDict,open("geo_WG_Dict.pack","wb"))
	



buildDomainWordsDict()



