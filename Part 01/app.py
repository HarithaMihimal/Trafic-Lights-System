from flask import Flask, jsonify, render_template
import time
from threading import Thread

app = Flask(__name__)

traffic_lights = {
    'north_south': 'red',
    'east_west': 'green'
}

def control_traffic_lights():
    while True:
        # North-South green, East-West red
        traffic_lights['north_south'] = 'green'
        traffic_lights['east_west'] = 'red'
        print("North-South: green, East-West: red")
        time.sleep(10)
        
        # North-South yellow, East-West red
        traffic_lights['north_south'] = 'yellow'
        traffic_lights['east_west'] = 'red'
        print("North-South: yellow, East-West: red")
        time.sleep(2)
        
        # North-South red, East-West green
        traffic_lights['north_south'] = 'red'
        traffic_lights['east_west'] = 'green'
        print("North-South: red, East-West: green")
        time.sleep(10)
        
        # North-South red, East-West yellow
        traffic_lights['north_south'] = 'red'
        traffic_lights['east_west'] = 'yellow'
        print("North-South: red, East-West: yellow")
        time.sleep(2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    print("Returning traffic light status:", traffic_lights)
    return jsonify(traffic_lights)

def start_traffic_light_thread():
    thread = Thread(target=control_traffic_lights)
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    start_traffic_light_thread()
    app.run(debug=True)
