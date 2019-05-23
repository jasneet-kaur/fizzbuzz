import operator 
import string




def depunct(line):
        for each in string.punctuation:
                line=line.replace(each," ")
        return(line)
def l33t_code(file):
        mylist1=['o','O']
        mylist2=['a','A']
        mylist3=['e','E']
        mylist4=['i','I']
        mylist5=['er']
        myfile=open(file,"w")
        for line in myfile:
                line=line.strip()
                line=depunct(line)
                line=line.split()
                for word in line:
                        for char in word:
                           if char in mylist1:
                                char=char.replace(char,"0")
                           elif char in mylist2:
                                char=char.replace(char,"4")
                           elif char in mylist3:
                                char=char.replace(char,"3")
                           elif char in mylist4:
                                char=char.replace(char,"1")
                        if word.endswith(mylist5):
                                word=word.replace(word,"xor")
                        else:   
                                pass
        return(mylist)
#print(l33t_code(“20k.txt”))
#printxy


def menu():
        targeted_file=print((input("enter the targeted file"))
        no_of_pages=print(int(input("enter pages you want to copy to another file"))
        l33t_code(targeted_file)        


menu()

