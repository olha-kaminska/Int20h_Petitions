#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 2018

@author: Oleh
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config') # configuration file


from app import views
