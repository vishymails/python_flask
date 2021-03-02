# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:30:25 2021

@author: SushiMahi
"""


from flask import Flask, redirect, url_for, request

app = Flask(__name__)



@app.route('/success/<user>')
def successMessage(user) :
    return ('Login Successful : %s' % user)


@app.route('/login', methods = ['POST', 'GET'])
def login() :
    if request.method == 'GET' :
        user = request.form['user']
        password = request.form['pwd']
        ack = user + "with pwd" + password
        return redirect(url_for('successMessage', user = ack))
    else : 
        user = request.form['user']
        password = request.form['pwd']
        ack = user + "with pwd" + password
        return redirect(url_for('successMessage', user = ack))



    
if __name__ == "__main__" :
    app.run("localhost", 8080)