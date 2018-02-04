#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Oleh
"""

from app import app
from flask import render_template, flash, request
from .forms import InputTextForm
from .nlp3o import TextAnalyser
from .inputhandler import getSampleText
import numpy
import math
import pandas
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import sys
import codecs
import operator
import datetime
from datetime import datetime
from collections import Counter
import re

 

    # Submit button in web for pressed
@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def manageRequest():

      # some useful initialisation
    theInputForm = InputTextForm()
    userText = "і не лишайте поле порожнім!"
    typeText = "Вам варто щось написати ..."
    language = "UA"
    text_len = 0
    
 #    lex_diff = True
 #   prob_det = True 
 #  no_caps = True
    lex_diff_sentence = "Намагайтеся використовувати більш професійну лексику.\n"
    prob_det_sentence = "Опишіть проблему більш детально, будь ласка.\n"
    no_caps_sentence = "Не використовуйте капс, будь ласка.\n"
    advices = ""
    nltk.download('punkt')
   
    
    if len(theInputForm.inputText.data)>0:
        userText = theInputForm.inputText.data
        typeText = "Ваш текст:"
        language = "UA" # which language?
        text_len = len(userText)


    myText = TextAnalyser(userText, language) # new object

    if len(userText) > 99:
        fragment = userText[:99] + " ..."
    else:
        fragment = userText
# advices
    def numericfeat(text):
        
        #sentences, words and word types
        words = word_tokenize(text)
        sents = sent_tokenize(text)
        #for i in range(len(text)):
        #    words += word_tokenize(text[i])
        #    sents += sent_tokenize(text[i])
    
        nwords = len(words)
        nsents = len(sents)
       # print(words)
        #print(sents)
        #print(text)
    
        #caps detect
        caps = 0
        for i in range (0, nwords):
            if words[i] == words[i].upper():
                caps += 1
        caps_freq = caps/nwords

        #the average length of the sentences
        lens = []
        for i in range (0, nsents):
            lens.append(len(sents[i]))
        avg_sent_length = numpy.mean(lens)
    
        #the average length of the words
        distinct_word_lengths = []    
        for i in range (0, nwords):
            distinct_word_lengths.append(len(words[i]))
        avg_word_length = numpy.mean(distinct_word_lengths)
        
        avg_sents = round(avg_sent_length/avg_word_length)
        avg_words = round(avg_word_length)
    
        truefalse = []
        #first value - avarage number of words in sentences, for good should be > 25
        if avg_sents > 26:
            truefalse.append(False)
        else:
            truefalse.append(True)
        print(avg_sents)
        #second value - avarage lenght of words, for good should be > 5
        if avg_words > 5:
            truefalse.append(False)
        else:
            truefalse.append(True)
        #thrird value - frequency of CAPS words, for good should be <= 0.19
        if caps_freq > 0.19:
            truefalse.append(True)
        else:
            truefalse.append(False)
        return words, truefalse        
            
    words, truemas = numericfeat(userText)  
 
    if truemas[1]:
        advices = advices + lex_diff_sentence
    if truemas[0]:
        advices = advices + prob_det_sentence
    if truemas[2]:
        advices = advices + no_caps_sentence
    if advices == "":
        advices = "Все ок!"
     

              # render the html page
    return render_template('results.html',
                       title='Результати аналізу',
                       inputTypeText = typeText,
                       originalText = fragment,
                       advicesStr = advices
                       )



  # render web form page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def initial():
      # render the initial main page
    return render_template('index.html',
                           title = 'Аналіз петицій',
                           form = InputTextForm())

@app.route('/results')
def results():
    return render_template('index.html',
                           title='Аналіз петицій')

  # render about page
@app.route('/about')
def about():
    return render_template('about.html',
                           title='Про проект')
