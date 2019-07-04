from fuzzywuzzy import fuzz
def search(query,list):
	out = ''
	best = 0 
	for element in list:
		temp = fuzz.token_set_ratio(element,query)
		if temp > best:
			out = element
			best = temp
	return out