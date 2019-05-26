# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:41:58 2019

@author: eupho
"""

from flask import Flask, jsonify , make_response
from flask import request

app = Flask(__name__)

#@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])

def results():
	

    # build a request object
    req = request.get_json()
    # fetch action from json
    action = req["responseId"]
    
    # return a fulfillment response
    return {'fulfillmentText': 'This is a response from webhook.'}
	
	
	
# create a route for webhook
@app.route('/', methods=['GET', 'POST'])
def webhook():

    # return response
    return make_response(jsonify(results()))
	
if __name__ == "__main__":
    app.run(debug=True)