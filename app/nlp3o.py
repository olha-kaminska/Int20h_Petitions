#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main module

Contains the class TextAnalyser to handle a text

NLP3O is a word game between NLP (Natural Language Processing) and C3PO

Created on Tue Apr 25 15:10:58 2017

@author: Mashimo
"""
"""from .inputhandler import readStopwords
import nltk
from nltk.stem import WordNetLemmatizer
"""

class TextAnalyser:
    
    'Text object, with analysis methods' 
    def __init__(self, inputText, language = "UA"):
        self.text = inputText
        self.language = language
        

        
    def length(self):
        """ return length of text in chars """
        return len(self.text)

    def findLongest(self):
      #Find the longest word in text1 and that word's length.
        longest = max(self.tokens, key=len)
        return (longest, len(longest))

