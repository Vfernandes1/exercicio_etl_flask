# import unittest
# from flask import Flask
# from app import db, app, WeatherData

# class TestYourApp(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#         self.app = app.test_client()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

#     def test_hello_world(self):
#         response = self.app.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b"Weather data has been stored in the database.", response.data)

#     def test_weather_data_stored(self):
#         response = self.app.get('/')
#         self.assertEqual(response.status_code, 200)

#         # Assuming that you have stored data for these cities
#         cities = ['New York', 'London', 'Tokyo', 'São Paulo', 'Chicago', 'Lima', 'Rio de Janeiro', 'Atlanta', 'Miami', 'Orlando', 'Fort Lauderdale', 'Campinas']

#         for city in cities:
#             self.assertTrue(WeatherData.query.filter_by(city=city).first())

# if __name__ == '__main__':
#     unittest.main()
