from rest_framework import viewsets, filters
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSetMixin
from nltk.corpus import stopwords 
from stop_words import get_stop_words
from nltk.stem import PorterStemmer
from datetime import datetime
from .models import *
from .serializers import *
import sys
import requests
import operator
import nltk
import json
import re

@api_view(['POST'])
def processText(request):
	def stemWord(word):
		size = len(word)
		if word[0:size-2] =='ed' or word[0:size-2] =='es':
			word = word[:-2]
		elif word[0:size-3] == 'ing':
			word = word[:-3]
		elif word[0:size-1] == 's':
			word = word[:-1]
		return word

	if(request.method=='POST'):
		try: 
			ps = PorterStemmer() 
			response = {}
			wordDict = {}
			response['result'] = []
			response['all'] = []
			result = []
			allWords = []
			text_string = request.data['data']
			text_string = text_string.replace("'",'').replace('-','').replace('_','')
			textContents = re.findall(r'\w+', text_string)
			print(textContents)
			for word in textContents:
				word = word.lower()
				# word = stemWord(word)
				word = ps.stem(word)
				if word in wordDict:
					temp = wordDict[word]
					wordDict[word] = temp + 1
				else:
					wordDict[word] = 1
			sorted_dict = sorted(wordDict.items(), key=lambda kv: (-kv[1],kv[0]))
			k = 0
			for item in sorted_dict:
				if k < 25:
					result.append(
						{'word':item[0],
						'frequency':item[1]})
				allWords.append({'word':item[0],
						'frequency':item[1]})
				k += 1
			response['result'] = result
			response['all'] = allWords
			return Response(response,status = status.HTTP_200_OK)
		except Exception as e:
			return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def disableStopWords(request):
	if(request.method=='POST'):
		try: 
			response = []
			words = request.data
			stop_words = list(get_stop_words('en')) 
			k = 0
			for word in words:
				if k == 25:
					break;
				if word['word'] not in stop_words and k < 25:
					response.append(word)
					k+=1
			return Response(response,status = status.HTTP_200_OK)
		except Exception as e:
			return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def saveWords(request):
	if(request.method=='POST'):
		try: 
			response = []
			results = request.data
			stopword = results['stop']
			time = datetime.now()
			text = results['text']
			words = []
			for word in results['words']:
				json_obj = json.dumps(word)
				words.append(json_obj)
			# myList = ','.join(words)
			serializer = AnalysisSerializer(data={'stopword':stopword,'words':words,'timestamp':time,'text':text})
			if(serializer.is_valid()):
			    serializer.save()
			    response.append(serializer.data)
			else:
				print(serializer.errors)
				return Response(status=status.HTTP_400_BAD_REQUEST)
			return Response(response,status = status.HTTP_200_OK)
		except Exception as e:
			return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getResults(request):
	if(request.method=='GET'):
		try: 
			response = []
			results = Analysis.objects.order_by('-timestamp')
			k = 0
			for result in results:
				if k == 10:
					break;
				serializer = AnalysisSerializer(result)
				response.append(serializer.data)
				k+=1
			return Response(response,status = status.HTTP_200_OK)
		except Exception as e:
			return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getText(request, resultid):
	if(request.method=='GET'):
		try: 
			result = Analysis.objects.get(id=resultid)
			response = result.text
			return Response(response,status = status.HTTP_200_OK)
		except Exception as e:
			return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getWords(request, resultid):
	if(request.method=='GET'):
		try: 
			response = []
			result = Analysis.objects.get(id=resultid)
			dataList = result.words
			print(dataList)
			for json_obj in dataList:
				temp_dict = json.loads(json_obj)
				response.append(temp_dict)
			print(response)
			return Response(response,status = status.HTTP_200_OK)
		except Exception as e:
			return Response(status = status.HTTP_400_BAD_REQUEST)