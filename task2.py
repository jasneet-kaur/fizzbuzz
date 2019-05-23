# copied from https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/ 


import string
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

dirNAme='/home/Fizzbuzz-jasneet'
listOfFiles = getListOfFiles(dirName)



def depunct(line):
	for each in string.punctuation:
		line=line.replace(each,””)
	return(line)


def character_word_count(listofFiles):
	mydict={}
	myfile=open(listofFiles,’r’)
	for line in myfile:
		line=line.strip()
		line=depunct(line)
		line=line.split()
		for word in line:
			if word in mydict.keys():
				pass
			else:
				mydict[word]=len(word)
	return(mydict)
print(character_word_count(listofFiles))




