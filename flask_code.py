# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:41:58 2019

@author: eupho
"""

from flask import Flask, json
from flask import request

app = Flask(__name__)

#@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])

@app.route('/')
def user():   
    return request.method
    