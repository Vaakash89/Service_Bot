# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:41:58 2019

@author: eupho
"""

from flask import Flask, json
from flask import request

app = Flask(__name__)

#@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])

@app.route('/',methods=['GET', 'POST'])
def user():   
    if(request.method == 'POST'):
        #data = request.form['user']['userId']
        content = request.json
        if(content['inputs'][0]['arguments'][0]['textValue'] == 'euphoric.aakash@gmail.com'):
            data = {'facebook':"Thanks God"}
            return json.dumps(data)
    
if __name__ == "__main__":
    app.run(debug=True)