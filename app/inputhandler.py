#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Oleh

"""
import os

  # samples are in the form (filename,title)
N_SAMPLES = 3
FILENAME = 0  #filename index
TITLE = 1  # title index
samples = [("Error!", "Error!"),
           ("moby-dick.txt", "Moby Dick novel"),
           ("marinetti.txt", "Marinetti poems"),
           ("urteil.txt", "Das Urteil novel"),
           ]

def getSampleText(sampleID):
    '''
    returns sample text as tuple of strings: (text, title) 
    
    Assume that a text file with the name as specified in variable samples
    above exists in the folder app/static
    '''    
    if sampleID < 0 or sampleID > N_SAMPLES:
        return (samples[0][0])
        
    filename = samples[sampleID][FILENAME] # get file name
        # the current directory is the root one
    path = os.path.join("app/static/", filename)
    file = open(path, 'r', encoding="utf-8")
    
    return (file.read(), samples[sampleID][TITLE]) 


def readStopwords(language):
    '''
    returns stopwords as strings
    
    Assume that a file called "stopwords<2chard-language-code>.txt
    exists in the folder app/static
    '''    
    filename = "stopwords" + language + ".txt"
    path = os.path.join("app/static/", filename)
    file = open(path, 'r')
    return file.read().splitlines()  # splitlines is used to remove newlines
