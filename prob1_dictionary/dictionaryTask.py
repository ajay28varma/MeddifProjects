thisdict = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

def group_by_owners(thisdict):
	returnDict = {}
	while len(thisdict) > 0 :
		tempList =[]
		auther_value = thisdict.get(list(thisdict.keys())[0])
		for key in thisdict.keys():
			if(thisdict.get(key) == auther_value) :
				tempList.append(key)
				thisdict.pop(key)
		returnDict[auther_value] = tempList
	return returnDict
print("Initial dictionary", thisdict)
print("Final dictionary ", group_by_owners(thisdict))
