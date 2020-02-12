from flask import Flask
from distance_sensor import Measurer
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/distance')
def getDistance():
    mes1 = Measurer(1,1)
    return mes1.measureDistance();

if __name__ == '__main__':
    app.run()
