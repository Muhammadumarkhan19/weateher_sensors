import Adafruit_DHT
import smbus2
import bme280
import time

# DHT11 ke liye setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin where DHT11 is connected

# BMP280 ke liye setup
bus = smbus2.SMBus(1)  # I2C bus number for Raspberry Pi 4
bme280_address = 0x76  # BMP280 address (check your sensor's address)

# Function to read BMP280
def read_bmp280():
    bme280.load_calibration_params(bus, bme280_address)
    data = bme280.sample(bus, bme280_address)
    return data.temperature, data.pressure

while True:
    # DHT11 se data read karna
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    # BMP280 se data read karna
    bmp_temp, pressure = read_bmp280()

    # Output print karna
    if humidity is not None and temperature is not None:
        print(f"DHT11 - Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%")
    else:
        print("DHT11 reading failed")

    print(f"BMP280 - Temperature: {bmp_temp:.1f}°C, Pressure: {pressure:.1f} hPa")

    time.sleep(2)  # 2 seconds delay


# import time
# import board
# import adafruit_dht
# import smbus2
# import bme280
# import pytz
# from i2c_lcd import i2c_lcd
# from flask import Flask, render_template, jsonify
# import threading

# # Initialize Flask
# app = Flask(__name__)

# # Sensor data pin is connected to GPIO 16 for DHT11
# dht_sensor = adafruit_dht.DHT11(board.D16)

# # BME280 sensor address
# bme280_address = 0x76
# bus = smbus2.SMBus(1)
# calibration_params = bme280.load_calibration_params(bus, bme280_address)

# lcd_instance = i2c_lcd.lcd() 
# lcd_instance.lcd_clear()

# # Shared data variable
# sensor_data = {
#     'temperature_c': None,
#     'humidity': None,
#     'pressure': None
# }

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/sensor_data')
# def sensor_data_route():
#     return jsonify(sensor_data)

# def read_sensors():
#     global sensor_data
#     while True:
#         try:
#             # Read DHT11 sensor data
#             temperature_c = dht_sensor.temperature
#             humidity = dht_sensor.humidity

#             # Read BME280 sensor data
#             bme_data = bme280.sample(bus, bme280_address, calibration_params)
#             pressure = bme_data.pressure

#             # Update sensor data
#             sensor_data['temperature_c'] = temperature_c
#             sensor_data['humidity'] = humidity
#             sensor_data['pressure'] = pressure

#             # Display readings on LCD
#             lcd_instance.lcd_display_string(f"Temp={temperature_c}°C", 1)
#             lcd_instance.lcd_display_string(f"Humidity={humidity}%", 2)
#             lcd_instance.lcd_display_string(f"Pressure={pressure:.2f}hPa", 3)

#             print(f"Temp={temperature_c}°C, Humidity={humidity}%, Pressure={pressure:.2f}hPa")
#             time.sleep(5)

#         except RuntimeError as error:
#             print("DHT Read Error:", error.args[0])
#             time.sleep(0.5)
#             continue
#         except Exception as e:
#             print('An unexpected error occurred:', str(e))
#             break

# if __name__ == '__main__':
#     # Start the sensor reading in a separate thread
#     sensor_thread = threading.Thread(target=read_sensors)
#     sensor_thread.start()
    
#     app.run(debug=True)





# import time
# import board
# import adafruit_dht
# import smbus2
# import bme280
# import pytz
# from i2c_lcd import i2c_lcd

# # Sensor data pin is connected to GPIO 16 for DHT11
# dht_sensor = adafruit_dht.DHT11(board.D16)

# # BME280 sensor address
# bme280_address = 0x76
# bus = smbus2.SMBus(1)
# calibration_params = bme280.load_calibration_params(bus, bme280_address)

# lcd_instance = i2c_lcd.lcd() 
# lcd_instance.lcd_clear()

# # Loop to read data
# running = True
# while running:
#     try:
#         # Read DHT11 sensor data
#         temperature_c = dht_sensor.temperature
#         humidity = dht_sensor.humidity
        
#         # Check for None values
#         if temperature_c is None or humidity is None:
#             print("DHT11 read error: Temperature or Humidity is None")
#             continue

#         # Read BME280 sensor data
#         bme_data = bme280.sample(bus, bme280_address, calibration_params)
#         pressure = bme_data.pressure
# @app.route('/')
# def index():
#     return render_template('index.html')
#         # Check for None value in pressure
#         if pressure is None:
#             print("BME280 read error: Pressure is None")
#             continue

#         # Display readings on LCD
#         lcd_instance.lcd_display_string(f"Temp={temperature_c}°C", 1)
#         lcd_instance.lcd_display_string(f"Humidity={humidity}%", 2)
#         lcd_instance.lcd_display_string(f"Pressure={pressure:.2f}hPa", 3)

#         print(f"Temp={temperature_c}°C, Humidity={humidity}%, Pressure={pressure:.2f}hPa")
#         time.sleep(5)

#     except RuntimeError as error:
#         print("DHT Read Error:", error.args[0])
#         time.sleep(0.5)
#         continue
#     except KeyboardInterrupt:
#         print('Program stopped')
#         running = False
#     except Exception as e:
#         print('An unexpected error occurred:', str(e))
#         running = False






# WORKING CORRECTLY

# import time
# import board
# import adafruit_dht
# import smbus2
# import bme280
# import pytz
# from i2c_lcd import i2c_lcd
# import firebase_admin
# from firebase_admin import credentials, db

# # Initialize Firebase Admin SDK
# cred = credentials.Certificate('/home/aptech/bmp280_project/iot-ultron.json')  # Update with your file path
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://iot-ultron-default-rtdb.firebaseio.com/'  # Update with your database URL
# })

# # Sensor data pin is connected to GPIO 16 for DHT11
# dht_sensor = adafruit_dht.DHT11(board.D16)

# # BME280 sensor address
# bme280_address = 0x76
# bus = smbus2.SMBus(1)
# calibration_params = bme280.load_calibration_params(bus, bme280_address)

# lcd_instance = i2c_lcd.lcd() 
# lcd_instance.lcd_clear()

# # Loop to read data
# running = True
# while running:
#     try:
#         # Read DHT11 sensor data
#         temperature_c = dht_sensor.temperature
#         humidity = dht_sensor.humidity

#         # Read BME280 sensor data
#         bme_data = bme280.sample(bus, bme280_address, calibration_params)
#         pressure = bme_data.pressure
#         timestamp = bme_data.timestamp

#         # Adjust timezone for the timestamp
#         desired_timezone = pytz.timezone('Europe/Lisbon')
#         timestamp_tz = timestamp.replace(tzinfo=pytz.utc).astimezone(desired_timezone)

#         # Prepare data for Firebase
#         data = {
#             'timestamp': timestamp_tz.strftime('%Y-%m-%d %H:%M:%S'),
#             'temperature_c': temperature_c,
#             'temperature_f': (temperature_c * 9/5) + 32,
#             'humidity': humidity,
#             'pressure': pressure
#         }
#         #  @app.route('/')
#         # def index():
#         #  return render_template('templates/index.html')
#         # Send data to Firebase
#         ref = db.reference('sensor_data')
#         ref.push(data)  # Push data as a new entry

#         # Print the readings to the console
#         print(f"{data['timestamp']} Temp={temperature_c:0.1f}ºC, "
#               f"Temp={data['temperature_f']:0.1f}ºF, Humidity={humidity:0.1f}%, "
#               f"Pressure={pressure:0.2f}hPa")

#         # Display readings on LCD
#         lcd_instance.lcd_display_string(f"Pressure={pressure:.2f}hPa", 1)
#         lcd_instance.lcd_display_string(f"Humidity={humidity:0.1f}%", 2)

#         time.sleep(5)

#     except RuntimeError as error:
#         # Handle DHT sensor read errors
#         print(error.args[0])
#         time.sleep(0.5)
#         continue
#     except KeyboardInterrupt:
#         print('Program stopped')
#         running = False
#     except Exception as e:
#         print('An unexpected error occurred:', str(e))
#         running = False


# import time
# import board
# import adafruit_dht
# import smbus2
# import bme280
# from i2c_lcd import i2c_lcd

# # Initialize DHT11 sensor on GPIO 16
# dht_sensor = adafruit_dht.DHT11(board.D16)

# # Initialize BME280 sensor
# bme280_address = 0x76
# bus = smbus2.SMBus(1)
# calibration_params = bme280.load_calibration_params(bus, bme280_address)

# # Initialize LCD
# lcd_instance = i2c_lcd.lcd()
# lcd_instance.lcd_clear()

# # Loop to read data and display on LCD
# running = True
# while running:
#     try:
#         # Read DHT11 sensor data
#         temperature_c = dht_sensor.temperature
#         humidity = dht_sensor.humidity

#         # Read BME280 sensor data
#         bme_data = bme280.sample(bus, bme280_address, calibration_params)
#         pressure = bme_data.pressure

#         # Clear the LCD and display the readings
#         lcd_instance.lcd_clear()
#         lcd_instance.lcd_display_string(f"Temp: {temperature_c}C", 1)
#         lcd_instance.lcd_display_string(f"Humi: {humidity}%", 2)
#         lcd_instance.lcd_display_string(f"P: {pressure:.2f}hPa", 3)

#         print(f"Temp={temperature_c}°C, Humidity={humidity}%, Pressure={pressure:.2f}hPa")
#         time.sleep(5)

#     except RuntimeError as error:
#         print("DHT Read Error:", error.args[0])
#         time.sleep(0.5)
#         continue
#     except KeyboardInterrupt:
#         print('Program stopped')
#         running = False
#     except Exception as e:
#         print('An unexpected error occurred:', str(e))
#         running = False
