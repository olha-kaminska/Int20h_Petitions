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
      # POST - retrieve all user submitted data

    # DEBUG flash('the book selected is: %s' % inputFromBook)

   
    if len(theInputForm.inputText.data)>0:
        userText = theInputForm.inputText.data
        typeText = "Ваш текст:"
        language = "UA" # which language?
        text_len = len(userText)

    # DEBUG flash('read:  %s' % typeText)


          # Which kind of user action ?


               # start analysing the text
    myText = TextAnalyser(userText, language) # new object
 

               # display all user text if short otherwise the first fragment of it
    if len(userText) > 99:
        fragment = userText[:99] + " ..."
    else:
        fragment = userText


              # render the html page
    return render_template('results.html',
                       title='Результати аналізу',
                       inputTypeText = typeText,
                       originalText = fragment,
                       numChars = text_len,
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
