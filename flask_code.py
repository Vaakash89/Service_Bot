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
    return make_response(json.dumps(results()))
	
if __name__ == "__main__":
    app.run(debug=True)