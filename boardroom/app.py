"""Boardroom functions."""
from flask import Flask
import requests
from flask import request
from params import *
import json
app = Flask(__name__)


################ FUNCTIONS ######################
def get_protocol_function(cname): 
    if cname is None:
        response = requests.get( API_BASE + "protocols")
    else:
        response = requests.get(API_BASE + "protocols/" + cname)

    if response.status_code == 200:
        data_json = response.json()
        return json.dumps(data_json)


def get_proposal_function(cname, refId): 
    if cname is None:
        response = requests.get(API_BASE + "proposals")
    if(cname is not None):
        response = requests.get( API_BASE + "protocols/" + cname + "/proposals")
    if(refId is  not None):
        response = requests.get(API_BASE + "proposals/" + refId)

    if response.status_code == 200:
        data_json = response.json()
        return json.dumps(data_json)



def get_voters_function(cname, refId, address): 
    if (cname is None and address is None and refId is None) :
        response = requests.get(API_BASE + "voters")

    if(cname is not None):
        print(API_BASE + "protocols/" + cname + "/voters")
        response = requests.get(API_BASE + "protocols/" + cname + "/voters")

    if(address is  not None):
        response = requests.get(API_BASE + "voters/" + address)

    if(refId is  not None):
        response = requests.get(API_BASE + "proposals/" + refId + "/votes")

    if response.status_code == 200:
        data_json = response.json()
        return json.dumps(data_json)

def get_stats_function ():
    response = requests.get(API_BASE + "stats")
    if response.status_code == 200:
        data_json = response.json()
        return json.dumps(data_json)

######################## APIs ################################## 
@app.route('/v1/protocols', methods=['GET'])
def get_protocol():
    cname = request.args.get('cname')
    if cname is None:
        result = get_protocol_function(cname = None)
    else:
        result = get_protocol_function(cname = cname)
    
    return json.loads(result)


@app.route('/v1/proposals', methods=['GET'])
def get_proposal():
    cname = request.args.get('cname')
    refId = request.args.get('refId')
    if cname is None:
        result = get_proposal_function(cname = None, refId = None)
    if(cname is not None):
        result = get_proposal_function(cname = cname, refId = None)

    if(refId is  not None):
        result = get_proposal_function(cname = None, refId = refId)

    return json.loads(result)


@app.route('/v1/voters', methods=['GET'])
def get_voters():
    cname = request.args.get('cname')
    address = request.args.get('address')
    refId = request.args.get('refId')
    if (cname is None and address is None and refId is None) :
        result = get_voters_function(cname = None, refId = None, address = None)
    if(cname is not None):
        result = get_voters_function(cname = cname, refId = None, address = None)
    if(address is  not None):
        result = get_voters_function(cname = None, refId = None, address = address)
    if(refId is  not None):
        result = get_voters_function(cname = None, refId = refId, address = None)

    return json.loads(result)

@app.route('/v1/stats', methods=['GET'])
def get_stats():
    result = get_stats_function()
    return result
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)



##### functions