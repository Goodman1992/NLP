import nltk
import re
import os
from beautifultable import BeautifulTable
global neg_g
global muti_g
#using objects to store data
class file():
    def __init__(self):
        file_name=None
        sents=None
        sents_tokenized=None
def trivialTokenizer(text):
   pattern = re.compile(r"\d+|Mr\.|Mrs\.|Dr\.|\b[A-Z]\.|[a-zA-Z_]+-[a-zA-Z_]+-[a-zA-Z_]+|[a-zA-Z_]+-[a-zA-Z_]+|[a-zA-Z_]+|--|'s|'t|'d|'ll|'m|'re|'ve|[.,:!?;\"'()\[\]&@#-]")
   return(re.findall(pattern, text))
#use this for directory path for emotions
def directory_input(prompt):
   path = input(prompt)
   if os.path.isdir(path):
      return path
   else:
      return file_name_input('Enter an existing file directory: ')
#use this for emotions, tokenize
def emotion_group(path):
    temp={}
    directory=os.fsencode(path)
    for f in os.listdir(directory):
        file = path+'/'+os.fsdecode(f)
        if file.endswith('.txt'):
            file_name=os.path.splitext(os.path.basename(file))[0]
            words=nltk.word_tokenize(open(file).read())
            temp[file_name]=words
    return temp

def file_name_input(prompt):
   path = input(prompt)
   if os.path.isfile(path):
      return path
   else:
      return file_name_input('Enter an existing file path: ')
#for a signle file, tokenize words by sentence
def file_set_up(file_path):
    new_file=file()
    file_sents_tokenized=[]
    file_name=os.path.splitext(os.path.basename(file_path))[0]
    file_sents=nltk.sent_tokenize(open(file1_path).read())
    for index in range(0,len(file_sents)):
        file_sents[index]=file_sents[index].replace('\n',' ')
    for item in file_sents:
        file_sents_tokenized.append(trivialTokenizer(item))
    new_file.file_name=file_name
    new_file.sents=file_sents
    new_file.sents_tokenized=file_sents_tokenized
    return new_file
#for a given file, if an item is in emotions, check prefixes
def find_e_word(obj,keys,e_dict):
    global neg_g
    global muti_g
    for index,item in enumerate(obj):
        for key in keys:
            if item in e_dict[key]:
                if index==0:
                    pass
                    #definitly positive emotion
                    #increase count of key
                else:
                    i=0
                    j=0
                    #have problem with recursive function, using global var as alternative
                    i,j=find_sequence(index-1,obj,negationTokens,intensifiers,0,0,0)
                    if j!=0 or i!=0:
                        print(item,' - ',key)
                        print(obj)
                        print(neg_g,' - ',muti_g)
                        neg_g=0
                        muti_g=0
                    #possibly assign those value into file object or 
#depends on index, check if it is at beginning of file
def check_before(index):
    if index-1>=0:
        return True
    else:
        return False
#body of recursive function
def find_sequence(index,obj,negationTokens,intensifiers,neg,muti,num):
    #assign current neg and muti to global var
    global neg_g
    global muti_g
    neg_g=neg
    muti_g=muti
    #determine negetivity of emotion by neg%2
    if obj[index] in negationTokens:
        neg+=1
        if check_before(index):
            find_sequence(index-1,obj,negationTokens,intensifiers,neg,muti,num)
    #determine how strong the emotion by muti 
    elif obj[index] in intensifiers:
        muti+=5
        if check_before(index):
            find_sequence(index-1,obj,negationTokens,intensifiers,neg,muti,num)
    #can do more if specfic prefix is required
    return neg,muti
        
negationTokens = ['hardly','never', 'no', "none", 'not', 'nothing', 'nowhere']
intensifiers=['very','much',"extremely",'greatly','literally','totally','badly','so','quite']
e_path=directory_input('Please input directory for emotions text files: ')
e_dict=emotion_group(e_path)
e_dict_keys=list(e_dict.keys())
file1_path=file_name_input('Please input path for first file: ')
file2_path=file_name_input('Please input path for second file: ')
file_1=file_set_up(file1_path)
file_2=file_set_up(file2_path)
for item in file_1.sents_tokenized:
    find_e_word(item,e_dict_keys,e_dict)
for item in file_2.sents_tokenized:
    find_e_word(item,e_dict_keys,e_dict)
print('done')



