from flask import Flask, jsonify, render_template
import threading
import time

app = Flask(__name__)

traffic_status = {
    'north_south': 'red',
    'south_north': 'red',
    'east_west': 'green',
    'west_east': 'green'
}

def update_traffic_lights():
    global traffic_status
    while True:
        # North-South and South-North green, East-West and West-East red
        traffic_status = {
            'north_south': 'green',
            'south_north': 'green',
            'east_west': 'red',
            'west_east': 'red'
        }
        time.sleep(10)
        # North-South and South-North yellow
        traffic_status = {
            'north_south': 'yellow',
            'south_north': 'yellow',
            'east_west': 'red',
            'west_east': 'red'
        }
        time.sleep(3)
        # East-West and West-East green, North-South and South-North red
        traffic_status = {
            'north_south': 'red',
            'south_north': 'red',
            'east_west': 'green',
            'west_east': 'green'
        }
        time.sleep(10)
        # East-West and West-East yellow
        traffic_status = {
            'north_south': 'red',
            'south_north': 'red',
            'east_west': 'yellow',
            'west_east': 'yellow'
        }
        time.sleep(3)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify(traffic_status)

if __name__ == '__main__':
    threading.Thread(target=update_traffic_lights, daemon=True).start()
    app.run(debug=True)
