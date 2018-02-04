#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Oleh
"""

class TextAnalyser:
    
    'Text object, with analysis methods' 
    def __init__(self, inputText, language = "UA"):
        self.text = inputText
        self.language = language
        
    def length(self):
        """ return length of text in chars """
        return len(self.text)
        
    


