import smbus2
import bme280
import os
import time
import pytz
from datetime import datetime
from i2c_lcd import I2cLcd           ct

# BME280 sensor address (default address)
address = 0x76                                                     

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Load calibration parameters
calibration_params = bme280.load_calibration_params(bus, address)

# Initialize the LCD                        
lcd = I2cLcd(1, 0x27, 2, 16)  # Adjust the I2C address and dimensions as needed

# Create a variable to control the while loop
running = True

# Create a timestamped filename
filename = f'sensor_readings_bme280_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
file_exists = os.path.isfile(filename)
file = open(filename, 'a')

# Write the header to the file if it does not exist
if not file_exists:
    file.write('Time and Date, Temperature (ºC), Temperature (ºF), Humidity (%), Pressure (hPa)\n')

# Loop forever
while running:
    try:
        # Read sensor data
        data = bme280.sample(bus, address, calibration_params)

        # Extract temperature, pressure, humidity, and corresponding timestamp
        temperature_celsius = data.temperature
        humidity = data.humidity
        pressure = data.pressure
        timestamp = data.timestamp

        # Adjust timezone
        desired_timezone = pytz.timezone('Europe/Lisbon')  # Replace with your desired timezone
        timestamp_tz = timestamp.replace(tzinfo=pytz.utc).astimezone(desired_timezone)

        # Convert temperature to Fahrenheit
        temperature_fahrenheit = (temperature_celsius * 9/5) + 32

        # Print the readings
        output = (timestamp_tz.strftime('%H:%M:%S %d/%m/%Y') + 
                  f" Temp={temperature_celsius:0.1f}ºC, " +
                  f"Temp={temperature_fahrenheit:0.1f}ºF, " +
                  f"Humidity={humidity:0.1f}%, Pressure={pressure:0.2f}hPa")
        print(output)

        # Display on LCD
        lcd.clear()  # Clear previous data on LCD
        lcd.putstr(f'Temp: {temperature_celsius:.1f}C\nHum: {humidity:.1f}%')  # Display temperature and humidity

        # Save data to the file
        file.write(f"{timestamp_tz.strftime('%H:%M:%S %d/%m/%Y')}, {temperature_celsius:.2f}, " +
                   f"{temperature_fahrenheit:.2f}, {humidity:.2f}, {pressure:.2f}\n")

        time.sleep(5)

    except KeyboardInterrupt:
        print('Program stopped')
        running = False
    except Exception as e:
        print('An unexpected error occurred:', str(e))
        running = False
    finally:
        file.close()
