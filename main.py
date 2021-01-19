'''
created by - Aditya Mittal
just install the packages mentioned in requirements.txt file 
and enjoy playing with sentiment ananlyzer!!
'''

from textblob import TextBlob
a=input("type ur Sentence :- ")
b=TextBlob(a)
x=b.sentiment.polarity
if x<0:
    print ("negative")

elif x==0:
    print ("netural") 

elif x>0 and x<=1 :
    print("positive ")
