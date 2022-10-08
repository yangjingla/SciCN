

import imp


import os 
import json 


def merge_term():
    dic = {}
    with open('vocab.txt', 'w') as fp:
        for root, dirs, files  in os.walk('tech'):

            for file in files:
                file = os.path.join(root, file)
                print(file)
                with open(file, 'r') as f:
                    for line in f.readlines():
                        word =line.strip()
                        fp.write(word+'\n')
                        if dic.get(word, -1) !=-1:
                            dic[word] +=1
                        else:
                            dic[word] = 1
    print(len(dic))


def merge_stopwords():
    dic = {}
    with open('stopwords.txt', 'w') as fp:
        for root, dirs, files  in os.walk('stopwords-master'):

            for file in files:
                file = os.path.join(root, file)
                print(file)
                with open(file, 'r') as f:
                    for line in f.readlines():
                        word =line.strip()
                        fp.write(word+'\n')

                        if dic.get(word, -1) !=-1:
                            dic[word] +=1
                        else:
                            dic[word] = 1
    print(len(dic))

if __name__ == '__main__':
    merge_term()
    merge_stopwords()

        