from os import listdir
from os.path import isfile, join
import re
import numpy as np
import sys,getopt
# mypath = "documente_problema/"


# imi separa query-ul in componentele necesare
def splitter(words_str):
	alph ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	words_str = words_str + " "
	words = re.findall(r'\w+',words_str)
	word_index = 0
	splitter = [" "]
	i = 0
	while i < len(words_str):	
		if words_str[i] in alph:
			splitter.append(words[word_index])
			word_index = word_index + 1
			while words_str[i] in alph and i < len(words_str):
				i = i + 1
		if i >= len(words_str):
			break
		if words_str[i] == "&":
			i = i + 1
			splitter.append("&")
		if words_str[i] == "|":
			i = i + 1
			splitter.append("|")
		if words_str[i] == "(":
			splitter.append("(")
		if words_str[i] == ")":
			splitter.append(")")
		if words_str[i] == "!":
			splitter.append("!")
		i = i + 1
	splitter.append(" ")

	return splitter

def operation(arrx,arry,and_op,or_op):
	np_arrx = np.array(arrx)
	np_arry = np.array(arry)
	if and_op == 1:
		return np.bitwise_and(np_arrx,np_arry)
	if or_op == 1:
		return np.bitwise_or(np_arrx,np_arry)
def negate(arr):
	arra = []
	for i in range(len(arr)):
		if arr[i] == 1:
			arra.append(0)
		else:
			arra.append(1)
	return arra
def word_into_arr(word,dictlist,onlyfiles,mypath):
	arr = []
	for f in onlyfiles:
		f = mypath + f
		arr.append(dictlist[word][f])
	return arr
def query(element,index,dictlist,negation,words,onlyfiles,mypath):
	arrxy = []
	and_op = 0
	or_op = 0
	rez = []
	while index < len(element):
		if element[index] in words:
			a = word_into_arr(element[index],dictlist,onlyfiles,mypath)
			arrxy.append(a)
		if element[index] == "!":
			negation = 1
		if element[index] == "(" :
			inf = query(element,index + 1,dictlist,negation,words,onlyfiles,mypath)
			if element[index-1] == "!":
				negation = 0
			arrxy.append(inf[0])
			index = inf[1] + 1
		if element[index] == "&":
			and_op = 1
		if element[index] =="|":
			or_op = 1
		if len(arrxy) == 2:
			rez = operation(arrxy[0],arrxy[1],and_op,or_op)
			and_op = 0
			or_op = 0
			arrxy.clear()
			arrxy.append(rez)
		if element[index] == ")":
			if negation == 1:
				arrxy[len(arrxy) - 1] = negate(arrxy[len(arrxy) - 1])
			break
		index = index + 1
	info=[]
	info.append(arrxy[len(arrxy) - 1])
	info.append(index)
	return info

##############################
def main(argv,mypath): # mypath parameter
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	onlyfiles.sort()
	words_str = str(argv)
	words = re.findall(r'\w+',words_str)

	# compose de dictionary
	dictlist = {}
	for word in words:
		dictlist[word] = {}
	#inverse file with words
	for word in words:
		for f in onlyfiles:
			f = mypath + f
			with open(f) as file:
				lowcase_file = file.read()
				if word.lower() in lowcase_file.lower():
					dictlist[word][f] = 1
				else:
					dictlist[word][f] = 0
	#################################
	split = splitter(words_str)
	print(split)
	a=[]
	searched=[]
	if len(split) == 1:
		a = word_into_arr(split[0],dictlist,onlyfiles,mypath)
		file_arr = a[0]
	else:
		a = query(split,0,dictlist,0,words,onlyfiles,mypath)
		file_arr = a[0]
	for i in range(len(file_arr)):
		if file_arr[i] == 1:
			searched.append(onlyfiles[i])
	if searched == []:
		searched = "No results"
	return searched
# arr=[]
# for word in words:
# 	for f in onlyfiles:
# 		f = "documente_problema/" + f
# 		arr.append(dictlist[word][f])

# matrix = np.array(arr)
# matrix = np.reshape(matrix,(len(words),len(onlyfiles)))
# print(matrix)
#word_index = 0
