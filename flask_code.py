# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:41:58 2019

@author: eupho
"""

from flask import Flask, jsonify ,json, make_response
from flask import request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
#@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])

def results():
	

    # build a request object
    req = request.get_json()
    # fetch action from json
    action = req["queryResult"]["queryText"]
    text = {}
    text['fulfillmentText'] = 'This is a response from webhook.'
    text['fulfillmentMessages'] = [None]*1
    text['fulfillmentMessages'][0] = {}
    text['fulfillmentMessages'][0]['facebook'] = {}
    text['fulfillmentMessages'][0]['facebook']['attachment'] = {}
    text['fulfillmentMessages'][0]['facebook']['attachment']['type'] = 'template'
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload'] = {}
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['template_type'] = 'button'
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['text'] = 'Available Service Centers'
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['buttons'] = [None] * 2
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['buttons'][0] = {}
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['buttons'][0]['type'] = 'postback'
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['buttons'][0]['payload'] = 'XYZ Car Comp'
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['buttons'][0]['title'] = 'XYZ Car Comp'
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['buttons'][1] = {}
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['buttons'][1]['type'] = 'postback'
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['buttons'][1]['payload'] = 'ABC Car Care'
    text['fulfillmentMessages'][0]['facebook']['attachment']['payload']['buttons'][1]['title'] = 'ABC Car Care'
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
    return make_response(json.dumps(results()))
	
if __name__ == "__main__":
    app.run(debug=True)