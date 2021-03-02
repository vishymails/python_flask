# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:35:04 2021

@author: SushiMahi
"""

from flask import Flask, redirect, url_for

app = Flask(__name__)



@app.route('/manager')
def work1() :
    return ("Assign modules to developer")


@app.route('/developer/<developerName>')
def work2(developerName) :
    return 'Work accepted by : %s' % developerName



@app.route('/company/<role>')
def workAssign(role) :
    if role == 'manager' :
        return redirect(url_for('work1'))
    else :
        return redirect(url_for('work2', developerName = role))
    
    
    
if __name__ == "__main__" :
    app.run("localhost", 8080)