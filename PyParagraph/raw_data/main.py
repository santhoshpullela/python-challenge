import pandas as pd 
import csv 
import re
import os 
import sys

para_data = os.path.join('raw_data',input("Please enter the filename: "))

# Open text file and read the file
f = open(para_data, 'r')
string = f.read()
ltrcount = len(string)
# Calculate the required counts and averages
wcount = len(re.findall("[a-zA-Z_]+", string))
wcount
sentences = re.split(r'[!?]+|(?<!\.)\.(?!\.)', string.replace('\n',''))
sentences = sentences[:-1]
sentence_count = len(sentences)
avg_letter = round((ltrcount/wcount),2)
avg_sentence = round((wcount/sentence_count),2)
# Write Output to Terminal and Text File
temp = sys.stdout
sys.stdout = open('Output.txt', 'w')
print("**** Paragraph Analysis ****" + "\n" + "------------------------------")
print("Approximate Word Count: " + str(wcount)) 
print("Approximate Sentence Count:  " + str(sentence_count))
print("Average Letter Count:  " + str(avg_letter)) 
print("Average Sentence Length: : " + str(avg_sentence))  
sys.stdout.close()
sys.stdout = temp
print("**** Paragraph Analysis ****" + "\n" + "------------------------------")
print("Approximate Word Count: " + str(wcount)) 
print("Approximate Sentence Count:  " + str(sentence_count))
print("Average Letter Count:  " + str(avg_letter)) 
print("Average Sentence Length: : " + str(avg_sentence))
