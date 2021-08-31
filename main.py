import flask
from flask import request, jsonify
import csv
import json

app = flask.Flask(__name__)

# For Debugging
# app.config["DEBUG"] = True

def make_json(csvFilePath, jsonFilePath, format):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows[format]
            data[key] = rows
 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

make_json(r'data_latest.csv', r'iso2.json', 'iso2')
make_json(r'data_latest.csv', r'iso3.json', 'iso3')
make_json(r'data_latest.csv', r'data_latest.json', 'Country,Other')


with open('iso2.json') as json_file:
    iso2 = json.load(json_file)
with open('iso3.json') as json_file:
    iso3 = json.load(json_file)
with open('data_latest.json') as json_file:
    data = json.load(json_file)

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return "Hello World!"

@app.route('/api/all', methods = ['GET'])
def all():
    return jsonify(data)

@app.route('/api/world', methods = ['GET'])
def world():
    return jsonify(data['World'])

@app.route('/api/country', methods = ['GET'])
def country():
    if 'req' in request.args:
        req = str(request.args['req'])
        req = req.upper()
        # Checking ISO2 or ISO3
        # if len(req) == 2:
        #     iso2 = req
        # elif len(req) == 3:
        #     iso3 = req
    else:
        return "Error: No valid ISO2 or ISO3 country code provided."
    
    # results_iso2 = []
    # results_iso3 = []

    if len(req) == 2:
        for i in iso2:
            if i == req:
                results_iso2 = (iso2[i])
        return jsonify(results_iso2)
    elif len(req) == 3:
        for j in iso3:
            if j == req:
                results_iso3 = (iso3[j])
        return jsonify(results_iso3)
    else:
        return "Error: No valid ISO2 or ISO3 country code provided."

# For Debugging    
# app.run()

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80)