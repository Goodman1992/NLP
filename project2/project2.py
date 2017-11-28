import nltk
import re
import os
from beautifultable import BeautifulTable
class file():
    def __init__(self):
        file_name=None
        sents=None
        sents_tokenized=None
def trivialTokenizer(text):
   pattern = re.compile(r"\d+|Mr\.|Mrs\.|Dr\.|\b[A-Z]\.|[a-zA-Z_]+-[a-zA-Z_]+-[a-zA-Z_]+|[a-zA-Z_]+-[a-zA-Z_]+|[a-zA-Z_]+|--|'s|'t|'d|'ll|'m|'re|'ve|[.,:!?;\"'()\[\]&@#-]")
   return(re.findall(pattern, text))

def directory_input(prompt):
   path = input(prompt)
   if os.path.isdir(path):
      return path
   else:
      return file_name_input('Enter an existing file directory: ')
    
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
    
def file_set_up(file1_path,file2_path):
    file_1=file()
    file_2=file()
    file1_sents_tokenized=[]
    file2_sents_tokenized=[]
    file1_name=os.path.splitext(os.path.basename(file1_path))[0]
    file2_name=os.path.splitext(os.path.basename(file2_path))[0]
    file1_sents=nltk.sent_tokenize(open(file1_path).read())
    file2_sents=nltk.sent_tokenize(open(file2_path).read())
    for index in range(0,len(file1_sents)):
        file1_sents[index]=file1_sents[index].replace('\n',' ')
    for index in range(0,len(file2_sents)):
        file2_sents[index]=file2_sents[index].replace('\n',' ')
    for item in file1_sents:
        file1_sents_tokenized.append(trivialTokenizer(item))
    for item in file2_sents:
        file2_sents_tokenized.append(trivialTokenizer(item))
    file_1.file_name=file1_name
    file_2.file_name=file2_name
    file_1.sents=file1_sents
    file_2.sents=file2_sents
    file_1.sents_tokenized=file1_sents_tokenized
    file_2.sents_tokenized=file2_sents_tokenized
    return file_1,file_2
negationTokens = ['hardly', "n't", 'never', 'no', 'none', 'not', 'nothing', 'nowhere']
intensifiers=['very','much','extremely','greatly','literally','totally','badly','so','quite']

e_path=directory_input('Please input directory for emotions text files: ')
e_dict=emotion_group(e_path)
e_dict_keys=list(e_dict.keys())
file1_path=file_name_input('Please input path for first file: ')
file2_path=file_name_input('Please input path for second file: ')
file_1,file_2=file_set_up(file1_path,file2_path)
for i in range(0,5):
    print(file_1.sents_tokenized[i])



