import json

f=open("static/data.json", "r")

if f.mode == 'r':
    contents = f.read()
    print(contents)