
'''
enhance the accuracy of google recognition

author: backman

e-mail: backman.only@gmail.com

method: 
	1. transform words from google voice Recognition to Wade-Giles encode
	2. find domain language words by string matching (Wade-Giles encode)

'''
from pypinyin import pinyin, lazy_pinyin
import pypinyin
import pickle

def editDistance(str1,str2):

	dpTable=[[0 for x in range(len(str2)+1) ] for y in range(len(str1)+1 )]
#initial table
	for i in range(len(str2)+1):
		dpTable[0][i]=i

	for i in range(len(str1)+1):
		dpTable[i][0]=i

	for x in range(1,len(str2)+1):
		for y in range(1,len(str1)+1):

			if str2[x-1] == str1[y-1]:
				dpTable[y][x]=dpTable[y-1][x-1]
			else:
				dpTable[y][x]= min(dpTable[y-1][x-1]+1,dpTable[y-1][x],dpTable[y][x-1])+1

	

	return dpTable[len(str1)][len(str2)]

def similarity(str1,str2):

	str2="-".join(lazy_pinyin(str2))

	ED=editDistance(str1,str2)
	sLen= len(str2)

	value=(float(sLen-ED)/float(sLen ) *100.0)

	if 0<= value and value <=100.0 :
		return value
	else:
		return 0


	




def domainWordsCorrector(strs,threshold):

	candidates={}
	geoDict=pickle.load(open("geo_WG_Dict.pack","rb"))

	for obj in geoDict.keys():
		# calculate every words's ED value.
		value=similarity(obj,strs) 
		if value > threshold:
			candidates[str(geoDict[obj])]=value

	#find most similar one!!
	maxV=0.0
	result=""
	for obj in candidates.keys():

		if maxV < candidates[obj]:
			maxV=candidates[obj]
			result=str(obj)

	return (result,maxV)




