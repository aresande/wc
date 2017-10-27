# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:14:28 2017

@author: silval01
"""

def count_lines(data_file):
    text = ""
    n = 0
    for line in data_file:
        text += line   
        n += 1
    return (text,n)

def count_words(text):
    text_temp = text
    special_chars = "!@#$%^&*()-_+={}[]|\:;'<>?,./\""
    for c in special_chars:
        text_good = text_temp.replace(c, ' ')
        text_temp = text_good
    spaces = " "
    for i in range(100):    #How I can do this for n consecutive spaces
        text_good = text_good.replace(spaces, ' ')
        spaces += " "
    words = text_good.split(' ') 
    return (words,len(words))

def count_chars(words):
    n_char = 0
    for w in words:
        n_char += len(w)
    return n_char


#Load file
file_path = 'words.txt'
data_file = open(file_path, 'r')

lines = count_lines(data_file)
words = count_words(lines[0])
chars = count_chars(words[0])

print('lines:',lines[1],', words:',words[1],', chars:',chars)
data_file.close()