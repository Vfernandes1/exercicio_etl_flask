from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for storing weather data
class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    date_ingestion = db.Column(db.String(20), nullable=False)
    data_type = db.Column(db.String(20), nullable=False)
    usage = db.Column(db.String(50), nullable=False)

# Create the database tables within the application context
with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    api_key = '402d6b30685d4ddcf2b466aa8f35c18b'

    cities = ['New York', 'London', 'Tokyo', 'São Paulo', 'Chicago', 'Lima', 'Rio de Janeiro', 'Atlanta', 'Miami', 'Orlando', 'Fort Lauderdale', 'Campinas']

    for city in cities:
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        temperature = data['main']['temp']

        # Store data in the database within the application context
        with app.app_context():
            new_weather_data = WeatherData(
                city=city,
                temperature=temperature,
                unit='Kelvin',
                date_ingestion=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                data_type='OpenWeather',
                usage='Example Usage'
            )
            db.session.add(new_weather_data)
            db.session.commit()

    return 'Weather data has been stored in the database.' 

if __name__ == '__main__':
    app.run(debug=True, port=5001)
