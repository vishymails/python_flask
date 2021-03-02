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

def display() :
    return "Hello All welcome to Python API Development"

app.add_url_rule('/dis_url', 'dis_url', display)


if __name__ == "__main__" :
    app.run("localhost", 8080)