from flask import Flask, jsonify ,json, make_response
from flask import request
from flask_pymongo import PyMongo
import os

#MONGO_URI = os.environ.get('MONGODB_URI')

app = Flask(__name__)
#app.config['JSON_SORT_KEYS'] = False
#app.config['MONGO_URI'] = MONGO_URI

app.config['MONGO_URI'] = "mongodb://aakash:aakash_4@ds241578.mlab.com:41578/heroku_g42lh6sd"
#@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])

mongo = PyMongo(app)

def results():
    
    action = req["queryResult"]["queryText"]   
    
    main = []
    for i in mongo.db.Service_centers.find({}):
        if(i['city'].lower() == action.lower()):
            city = i['centers'][0]
            dummy = {"type": "postback",
                     "payload": city,
                     "title": city}
            main.append(dummy)    

    # build a request object
    req = request.get_json()
    # fetch action from json

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
                                                
                                              }
                                            }
                                    }      
                                }
        }
                                              
                                              
                                              
    text["payload"]["facebook"]["attachment"]["payload"]["buttons"] = main
     
                                              
    
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