from pypinyin import pinyin, lazy_pinyin
import pypinyin
from enhancer import domainWordsCorrector , domainWordExtractor ,teamExtractor
import speech_recognition as sr
import sys

from pywinauto.application import Application


'''
Functional Programming

先測試 長度3的字串
future  

'''
import time



def voiceToText():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		audio = r.listen(source)

	try:
		return r.recognize_google(audio,language="zh-TW")
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

	return None



def outputToNP(app,word):
	app.UntitledNotepad.Edit.type_keys(word)
	return app




#====================================================



app = Application().start("notepad.exe")

#====================Voice Recognition=============================







while True:
	input("")
	print ("請說話")
	sys.stdout.flush()
	rawText=voiceToText()
	print ("rawData: ",rawText)
	wordList=domainWordExtractor(rawText)
	#wordList=teamExtractor(rawText)

	if wordList is not None:

		print("資訊: ", wordList)

		correctText=""
		for obj in wordList:
			correctText+=obj
		outputToNP(app,correctText)

	else:
		print("沒聽到 :<")

