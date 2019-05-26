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
    action = req["queryResult"]["queryText"]
    text = {}
    text['facebook'] = {}
    text['facebook']['attachment'] = {}
    text['facebook']['attachment']['type'] = 'template'
    text['facebook']['attachment']['payload'] = {}
    text['facebook']['attachment']['payload']['template_type'] = 'button'
    text['facebook']['attachment']['payload']['text'] = 'Available Service Centers'
    text['facebook']['attachment']['payload']['buttons'] = [None] * 2
    text['facebook']['attachment']['payload']['buttons'][0] = {}
    text['facebook']['attachment']['payload']['buttons'][0]['type'] = 'postback'
    text['facebook']['attachment']['payload']['buttons'][0]['payload'] = 'XYZ Car Comp'
    text['facebook']['attachment']['payload']['buttons'][0]['title'] = 'XYZ Car Comp'
    text['facebook']['attachment']['payload']['buttons'][1] = {}
    text['facebook']['attachment']['payload']['buttons'][1]['type'] = 'postback'
    text['facebook']['attachment']['payload']['buttons'][1]['payload'] = 'ABC Car Care'
    text['facebook']['attachment']['payload']['buttons'][1]['title'] = 'ABC Car Care'
    if(action.lower() == "chennai" ):
        res = text
    else:
        res = "Not Chennai"
    
    # return a fulfillment response
    return res
	
	
	
# create a route for webhook
@app.route('/', methods=['GET', 'POST'])
def webhook():

    # return response
    return make_response(jsonify(results()))
	
if __name__ == "__main__":
    app.run(debug=True)