import json

def sth():
    jsonData = []
    with open('data.json', 'r') as f:
        jsonData = json.load(f)

    return jsonData

x1 = sth()['sensors'][0]['distance']
x2 = sth()['sensors'][1]['distance']
x3 = sth()['sensors'][2]['distance']

if x1 or x2 or x3 < 150:
    print("malakas")
