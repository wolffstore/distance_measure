from flask import Flask, render_template, request, jsonify
from SensorPi import SensorPi
from Sensor import Sensor
import threading
import json

app = Flask(__name__)


@app.route('/')
def malakas():
    sensor1 = SensorPi(1, 1, 7, 11)
    sensor2 = SensorPi(2, 2, 7, 13)
    sensor3 = SensorPi(3, 3, 7, 15)

    sensors = [sensor1, sensor2, sensor3]

    writeFile()

    return render_template('index.html', sensors=sensors)


def writecontinuously():
    while True:
        writeFile()


def writeFile():
    sensor1 = SensorPi(1, 1, 7, 11)
    sensor2 = SensorPi(2, 2, 7, 13)
    sensor3 = SensorPi(3, 3, 7, 15)

    jsonData = {}
    jsonData['sensors'] = []
    jsonData['sensors'].append({
        'id': sensor1.id,
        'side': sensor1.corridor,
        'distance': sensor1.calculateDistance()
    })

    jsonData['sensors'].append({
        'id': sensor2.id,
        'side': sensor2.corridor,
        'distance': sensor2.calculateDistance()
    })

    jsonData['sensors'].append({
        'id': sensor3.id,
        'side': sensor3.corridor,
        'distance': sensor3.calculateDistance()
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
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
