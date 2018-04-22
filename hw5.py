# -*- coding: utf-8 -*-
import csv
import json
import pickle
import string
from collections import Counter


def main(filename):
    
    txtfile=open(filename)
    lines = txtfile.readlines()

    
    all_words = []

    
    for line in lines:
        
        words =line.split()

        
        for word in words:
            
            word=word.strip("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+")
            
            if word:
                
                all_words.append(word)
  
    
    counter =Counter(all_words)

   
    
    with open("wordcount.csv", "w") as csv_file:
       
        writer =csv.writer(csv_file)
        
        writer.writerow(['word', 'count'])
        
        writer.writerows(counter.items())

   
    with open("wordcount.json", 'w') as f:
        json.dump(counter, f)
    
    
    pickle.dump(counter, open("wordcount.pkl", 'wb'))

if __name__ == '__main__':
    main("i_have_a_dream.txt")