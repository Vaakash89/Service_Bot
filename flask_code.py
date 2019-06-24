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
    
    req = request.get_json()  
    action = req["queryResult"]["queryText"]   
    
    main = []
    for i in mongo.db.Service_centers.find({}):
        if(i['city'].lower() == action.lower()):
            #for j in range(0,len(i['centers'])):
            for center in i['centers']:
                dummy = {"type": "postback",
                         "payload": center,
                         "title": center}
                main.append(dummy)    

    # build a request object

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
                                              
    if not main:
        text = {
              "fulfillmentText": "Sorry we dont serve in your city yet!",
              "fulfillmentMessages": []
              }
    else:
        text["payload"]["facebook"]["attachment"]["payload"]["buttons"] = main
    # return a fulfillment response
    return text
		
# create a route for webhook
@app.route('/', methods=['GET', 'POST'])
def webhook():

    # return response
    return make_response(jsonify(results()))
	
if __name__ == "__main__":
    app.run(debug=True)