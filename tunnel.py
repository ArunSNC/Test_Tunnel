from flask import Flask,jsonify,request,Response
from flask_frozen import Freezer
import json

app = Flask(__name__)
freezer = Freezer(app)
app.config["JSON_SORT_KEYS"] = False
app.config['CORS_HEADERS'] = 'application/json'


@app.route('/test/', methods=['POST'])
def test():
    myDict = {"sensor": "temperature", "identifier":"SENS123456789", "value":10, "timestamp": "20/10/2017 10:10:25"}
    return json.dumps(myDict)


if __name__ == "__main__":
    freezer.freeze()
    app.run(debug=True,port=9999)