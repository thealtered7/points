import json as js

def to_json(ob):
    """to_json takes an argument and calls to_json on it"""
    json_data = ob.to_json_dict()
    json_string = js.dumps(json_data, sort_keys=True, indent="\t")
    return json_string
