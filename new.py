import time
from i2c_lcd import i2c_lcd

# Create an instance of the LCD
lcd_instance = i2c_lcd.lcd()  # Initialize the LCD, no parameters as per the module structure

# Clear the LCD
lcd_instance.lcd_clear()

# Display some text
lcd_instance.lcd_display_string("Hello, World!", 1)  # Line 1
lcd_instance.lcd_display_string("Raspberry Pi", 2)    # Line 2

# Keep the message for 10 seconds
time.sleep(10)

# Clear the LCD before finishing
lcd_instance.lcd_clear()
