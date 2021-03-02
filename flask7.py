# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:20:58 2021

@author: SushiMahi
"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/caller/<name>')
def callback_function(name) :
    return render_template('flask7.htm', name = name)



if __name__ == "__main__" :
    app.run("localhost", 8080)