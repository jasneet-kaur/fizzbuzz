import operator
import string
import 20k.txt

def depunctuate(line):
		for repl in string.punctuation:
			line=line.replace(repl,"")
		return line
	
	
def unique_words(book):
	    unique_list=[]
	    for item in book:
	        #print(1)
	        for line in item:
	            #print(2)
	            line=line.strip()
	            line=depunctuate(line) 
	            line=line.split()
	            for word in line:
	                #print(3)
	                unique_list.append(word)
	    unique_list=set(unique_list)
	    if unique_list
	    return tuple(unique_list)

def unique_in20k(book):
	unique_words(book)
	if unique_list	
		
	book1=open("Book1.txt",'r')
	book2=open("Book1.txt",'r')
	book3=open("Book1.txt",'r')
	book4=open("20k.txt",'r')
	book_list=(book1,book2,book3,book4)
	unique_list=unique_words(book_list)
	print("The List of unique words in Three books::",unique_list)
	
	



