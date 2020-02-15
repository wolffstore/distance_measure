from flask import Flask, jsonify
from Sensor import Sensor
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/distance')
def sensor():
    sensorCorOne = Sensor(1,1,7,11)
    distOne = sensorCorOne.calculateDistance()
    return jsonify(
        {
            'id': sensorCorOne.id,
            'corridor': sensorCorOne.corridor,
            'distance': distOne
        }
    )

@app.route('/distances')
def sensors():
    sensorCorOne = Sensor(1,1,7,11)
    sensorCorTwo = Sensor(2,2,7,13)
    sensorCorThree = Sensor(3,3,7,15)

    distOne = sensorCorOne.calculateDistance()
    distTwo = sensorCorTwo.calculateDistance()
    distThree = sensorCorThree.calculateDistance()


    return jsonify(
        {
            'sensors': [
                {
                    'id': sensorCorOne.id,
                    'corridor': sensorCorOne.corridor,
                    'distance': distOne
                },
                {
                    'id': sensorCorTwo.id,
                    'corridor': sensorCorTwo.corridor,
                    'distance': distTwo
                },
                {
                    'id': sensorCorThree.id,
                    'corridor': sensorCorThree.corridor,
                    'distance': distThree
                }
            ]
        }
    ), 200

if __name__ == '__main__':
    app.run(debug=True)
