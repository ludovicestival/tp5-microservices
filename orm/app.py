from flask import Flask, jsonify
from models import db, WeatherData
from datetime import datetime

DB_HOST = 'db'
DB_PORT = 3306
DB_USER = 'weather'
DB_PASSWORD = 'weatherpass'
DB_NAME = 'weather_db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


coord = {
    'Rodez': (44.35, 2.57),
    'Honolulu': (21.30, -157.85),
    'Tombouctou': (16.77, -3.01)
}


@app.route('/weather/<city>', methods=['GET'])
def weather(city: str):
    if city not in coord:
        return jsonify({'error': 'unknown city'})
    
    result = WeatherData.query.filter_by(city=city).first()

    if result is None:
        latitude = coord[city]
        longitude = coord[city]

        data = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weath'

        result = WeatherData(
            city=city,
            temperature=data['temperature'],
            windspeed=data['windspeed'],
            condition=data['condition'],
            timestamp=datetime.now()
        )

        db.session.add(entry)
        db.session.commit()

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)