from pypinyin import pinyin, lazy_pinyin
import pypinyin
from enhancer import domainWordsCorrector
import speech_recognition as sr
import sys



'''
Functional Programming


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



print ("說！")
sys.stdout.flush()
time.sleep(1)


reText=voiceToText()

print (reText)
print (domainWordsCorrector(reText,70.0))


