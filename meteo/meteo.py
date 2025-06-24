from flask import Flask, request, jsonify

app = Flask(__name__)

coord = {
    'Rodez': (44.35, 2.57),
    'Honolulu': (21.30, -157.85),
    'Tombouctou': (16.77, -3.01)
}

@app.route('/weather/<city>', methods=['GET'])
def weather(city: str):
    if city not in coord:
        return jsonify({'error': 'unknown city'})

    latitude = coord[city]
    longitude = coord[city]

    data = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weath'

    result = {
        'city': data['city'],
        'temperature': data['temperature'],
        'windspeed': data['windspeed'],
        'condition': data['condition']
    }

    return jsonify(result)


@app.route('/cities', methods=['GET'])
def cities():
    return jsonify({'cities': coord.keys()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)