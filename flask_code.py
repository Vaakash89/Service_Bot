from flask import Flask, jsonify ,json, make_response
from flask import request
from flask_pymongo import PyMongo
import os

MONGO_URI = os.environ.get('MONGODB_URI')

app = Flask(__name__)
#app.config['JSON_SORT_KEYS'] = False
app.config['MONGO_URI'] = MONGO_URI
#@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])

mongo = PyMongo(app)

def results():
	

    # build a request object
    req = request.get_json()
    # fetch action from json
    action = req["queryResult"]["queryText"]
    text = {
              "fulfillmentText": "This is a text response",
              "fulfillmentMessages": [],
                                  "payload": {
                                    "facebook": {
                                         "attachment": {
                                              "type": "template",
                                              "payload": {
                                                "template_type": "button",
                                                "text": "Availabler Service Centers",
                                                "buttons": [
                                                  {
                                                    "type": "postback",
                                                    "payload": "XYZ Car Comp",
                                                    "title": str(mongo)
                                                  },
                                                  {
                                                    "type": "postback",
                                                    "payload": "ABC Car Care",
                                                    "title": "ABC Car Care"
                                                  }
                                                ]
                                              }
                                            }
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
    return make_response(jsonify(results()))
	
if __name__ == "__main__":
    app.run(debug=True)