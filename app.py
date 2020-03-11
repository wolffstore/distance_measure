from flask import Flask, render_template, request, jsonify
from Person import Person
from Sensor import Sensor
import threading
import json

app = Flask(__name__)


@app.route('/')
def malakas():
    sensor1 = Sensor(1, 1, 7, 11)
    sensor2 = Sensor(2, 2, 7, 13)
    sensor3 = Sensor(3, 3, 7, 15)

    sensors = [sensor1, sensor2, sensor3]

    writeFile()

    return render_template('index.html', sensors=sensors)


def writecontinuously():
    while True:
        writeFile()


def writeFile():
    sensor1 = Sensor(1, 1, 7, 11)
    sensor2 = Sensor(2, 2, 7, 13)
    sensor3 = Sensor(3, 3, 7, 15)

    jsonData = {}
    jsonData['sensors'] = []
    jsonData['sensors'].append({
        'id': sensor1.id,
        'side': sensor1.side,
        'distance': sensor1.getDistance()
    })

    jsonData['sensors'].append({
        'id': sensor2.id,
        'side': sensor2.side,
        'distance': sensor2.getDistance()
    })

    jsonData['sensors'].append({
        'id': sensor3.id,
        'side': sensor3.side,
        'distance': sensor3.getDistance()
    })

    with open('static/data.json', 'w') as outfile:
        json.dump(jsonData, outfile, indent=4)


@app.route('/begin', methods=['POST'])
def begin():
    thread = threading.Thread(target=writecontinuously)
    thread.start()

    return jsonify({'result': 'success'}), 200


@app.route('/update', methods=['POST'])
def update():
    person = Person("fotis", "alatas", 30)

    return jsonify({'result': 'success', 'name': person.name, 'age': person.age})


if __name__ == '__main__':
    app.run(debug=True)
