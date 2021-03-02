# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:09:59 2021

@author: SushiMahi
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world() :
    return "Hello IBM"

if __name__ == "__main__" :
    app.run()