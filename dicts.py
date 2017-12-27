print "Dicts are created using {} with : seperating key and values and , seperating entries in the dict"

nameGradeDict = {'aravind':3,'kumar':5,'temp':4}

print "Iterating through the keys and values in a dict"

for key,value in nameGradeDict.items():
    print("Key is %s" % key)
    print("Value is %d" % value)

nameGradeDict['aravind'] = 6

for key in nameGradeDict.keys():
    print("Key is %s" % key)

for value in nameGradeDict.values():
    print("Value is %d" % value)

