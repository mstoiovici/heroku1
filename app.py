# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:44:21 2019

@author: maria
"""

from flask import Flask,render_template
app=Flask("MyApp")

@app.route("/")
def index():
    return render_template("index.html", title="My Fourth App On Heroku", **locals())

app.run()
