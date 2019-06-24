from fuzzywuzzy import fuzz


#trim and make them lowercase elsewhere to decouple this program from the main one

def searchA(query,list):
	out = ''
	best = 0 
	for element in list:
		temp = fuzz.token_set_ratio(element,query)
		if temp > best:
			out = element
			best = temp
	return out

def searchB(query,list,list2):
	out = ''
	best = 0
	for element,element2 in zip(list,list2):
		temp = fuzz.token_set_ratio(element,query)+fuzz.token_set_ratio(element2,query)
		if temp > best:
			out = (element,element2)
			best = temp
	return out

