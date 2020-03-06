from flask import Flask, jsonify
from Sensor import Sensor
import threading
import time
import json
import requests
#from playsound import playsound

app = Flask(__name__)


# def run_job():
#     while True:
#         print("Run recurring task")
#         sensorCorOne = Sensor(1, 1, 7, 11)
#         sensorCorTwo = Sensor(2, 2, 7, 13)
#         sensorCorThree = Sensor(3, 3, 7, 15)
#
#         distOne = sensorCorOne.calculateDistance()
#         distTwo = sensorCorTwo.calculateDistance()
#         distThree = sensorCorThree.calculateDistance()
#
#         jsonData = {
#             'sensors': [
#                 {
#                     'id': sensorCorOne.id,
#                     'corridor': sensorCorOne.corridor,
#                     'distance': distOne
#                 },
#                 {
#                     'id': sensorCorTwo.id,
#                     'corridor': sensorCorTwo.corridor,
#                     'distance': distTwo
#                 },
#                 {
#                     'id': sensorCorThree.id,
#                     'corridor': sensorCorThree.corridor,
#                     'distance': distThree
#                 }
#             ]
#         }
#
#         with open('data.json', 'w', encoding='utf-8') as f:
#             json.dump(jsonData, f, ensure_ascii=False, indent=4)

# @app.before_first_request
# def activate_job():
#     def run_job():
#         while True:
#             print("Run recurring task")
#             sensorCorOne = Sensor(1, 1, 7, 11)
#             sensorCorTwo = Sensor(2, 2, 7, 13)
#             sensorCorThree = Sensor(3, 3, 7, 15)
#
#             distOne = sensorCorOne.calculateDistance()
#             distTwo = sensorCorTwo.calculateDistance()
#             distThree = sensorCorThree.calculateDistance()
#
#             jsonData = {
#                 'sensors': [
#                     {
#                         'id': sensorCorOne.id,
#                         'corridor': sensorCorOne.corridor,
#                         'distance': distOne
#                     },
#                     {
#                         'id': sensorCorTwo.id,
#                         'corridor': sensorCorTwo.corridor,
#                         'distance': distTwo
#                     },
#                     {
#                         'id': sensorCorThree.id,
#                         'corridor': sensorCorThree.corridor,
#                         'distance': distThree
#                     }
#                 ]
#             }
#
#             with open('data.json', 'w', encoding='utf-8') as f:
#                 json.dump(jsonData, f, ensure_ascii=False, indent=4)
#
#     thread = threading.Thread(target=run_job)
#     thread.start()

@app.route('/dist')
def dist():
    sensorCorOne = Sensor(1, 1, 7, 11)
    # sensorCorTwo = Sensor(2, 2, 7, 13)
    sensorCorThree = Sensor(3, 3, 7, 15)

    distOne = sensorCorOne.calculateDistance()
    # distTwo = sensorCorTwo.calculateDistance()
    distThree = sensorCorThree.calculateDistance()

    if distOne or distThree < 150.0:
        # playsound('Beep.mp3')
        return """
               <body style="text-align: center">  
                       <div style="width:500px;height:100px;border:1px solid #000;background-color:red;">You are too close</div>
                         <audio controls autoplay>
                           <source src="Beep.ogg" type="audio/ogg">
                           <source src="Beep.mp3" type="audio/ogg">
                       </audio> 
               </body>
           """

    else:
        return """
               <div style="width:500px;height:100px;border:1px solid #000;background-color:green;">You are fine</div>
           """

@app.route('/sensors')
def sensors():
    sensorCorOne = Sensor(1, 1, 7, 11)
    #sensorCorTwo = Sensor(2, 2, 7, 13)
    sensorCorThree = Sensor(3, 3, 7, 15)

    distOne = sensorCorOne.calculateDistance()
    #distTwo = sensorCorTwo.calculateDistance()
    distThree = sensorCorThree.calculateDistance()

    jsonData = {
        'sensors': [
            {
                'id': sensorCorOne.id,
                'corridor': sensorCorOne.corridor,
                'distance': distOne
            },
            # {
            #     'id': sensorCorTwo.id,
            #     'corridor': sensorCorTwo.corridor,
            #     'distance': distTwo
            # },
            {
                'id': sensorCorThree.id,
                'corridor': sensorCorThree.corridor,
                'distance': distThree
            }
        ]
    }

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/distance')
def sensor():
    sensorCorOne = Sensor(1, 1, 7, 11)
    distOne = sensorCorOne.calculateDistance()
    return jsonify(
        {
            'id': sensorCorOne.id,
            'corridor': sensorCorOne.corridor,
            'distance': distOne
        }
    )


@app.route('/numbers')
def number():
    jsonData = []
    with open('data.json', 'r') as f:
        jsonData = json.load(f)

    distance1 = jsonData['sensors'][0]['distance']
    distance2 = jsonData['sensors'][1]['distance']
    distance3 = jsonData['sensors'][2]['distance']

    if distance1 or distance2 or distance3 < 150.0:
        #playsound('Beep.mp3')
        return """
            <body style="text-align: center">  
                    <div style="width:500px;height:100px;border:1px solid #000;background-color:red;">You are too close</div>
                      <audio controls autoplay>
                        <source src="Beep.ogg" type="audio/ogg">
                        <source src="Beep.mp3" type="audio/ogg">
                    </audio> 
            </body>
        """

    else:
        return """
            <div style="width:500px;height:100px;border:1px solid #000;background-color:green;">You are fine</div>
        """


@app.route('/distances')
def sensors():
    jsonData = ""
    with open('data.json') as f:
        jsonData = json.load(f)

    return jsonify(jsonData), 200


# def start_runner():
#     def start_loop():
#         not_started = True
#         while not_started:
#             print('In start loop')
#             try:
#                 r = requests.get('http://127.0.0.1:5000/')
#                 if r.status_code == 200:
#                     print('Server started, quiting start_loop')
#                     not_started = False
#                 print(r.status_code)
#             except:
#                 print('Server not yet started')
#             time.sleep(2)
#
#     print('Started runner')
#     thread = threading.Thread(target=start_loop)
#     thread.start()


if __name__ == '__main__':
    app.run(debug=True)
