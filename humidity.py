import time
import board
import adafruit_dht

# Sensor data pin is connected to GPIO 16
sensor = adafruit_dht.DHT11(board.D16)

while True:
    try:
        # Read temperature and humidity
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity

        # Print the values
        print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))
    
    except RuntimeError as error:
        # Errors can happen while reading from DHT
        print(error.args[0])
        time.sleep(2.0)
        continue
    
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3.0)
