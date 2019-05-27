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
    text = {
              "fulfillmentText": "This is a text response",
              "fulfillmentMessages": [
                {
                  "card": {
                    "title": "card title",
                    "subtitle": "card text",
                    "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
                    "buttons": [
                      {
                        "text": "button text",
                        "postback": "https://assistant.google.com/"
                      }
                    ]
                  }
                }
              ],
              "source": "example.com",
              "payload": {
                "google": {
                  "expectUserResponse": True,
                  "richResponse": {
                    "items": [
                      {
                        "simpleResponse": {
                          "textToSpeech": "this is a simple response"
                        }
                      }
                    ]
                  }
                },
                "facebook": {
                  "text": "Hello, Facebook!"
                },
                "slack": {
                  "text": "This is a text response for Slack."
                }
              }
            }
    
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
    return jsonify(results())
	
if __name__ == "__main__":
    app.run(debug=True)
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