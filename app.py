from flask import Flask, json, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# home
@app.route('/', methods=['GET'])
def home():
    return jsonify('Page : Home')


# sanity check route
@app.route('/api/cars', methods=['GET'])
def api_cars():
    data = json.load(open('Data/Dataset-Hackathon.json'))
    return jsonify(data)


if __name__ == '__main__':
    app.run()
