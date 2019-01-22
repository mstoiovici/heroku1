# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:44:21 2019

@author: maria
"""

from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run()
