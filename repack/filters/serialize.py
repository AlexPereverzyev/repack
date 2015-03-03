
import json
import pickle

def json_encode(v):
    return json.dumps(v)

def json_decode(v):
    return json.loads(v)

def serialize(v):
    return pickle.dumps(v)

def deserialize(v):
    return pickle.loads(v)

