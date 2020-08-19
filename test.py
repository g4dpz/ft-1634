from ft817 import FT817
import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

# Constants
SERIAL_PORT0 = "/dev/ttyUSB_TX"
SERIAL_PORT1 = "/dev/ttyUSB_RX"
SAMPLES_PER_SEC = 5

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

if __name__ == '__main__':
    print ("Starting FT-817ND monitor...")
    
    try:

# Initialise I2C bus.
        i2c = busio.I2C(board.SCL, board.SDA)

# Initialise the LCD class
        lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

        lcd.clear()
# Set LCD color to red
        lcd.color = [100, 0, 0]
        ft817_0 = FT817(SERIAL_PORT0)
        ft817_1 = FT817(SERIAL_PORT1)
        delay = 1.0 / SAMPLES_PER_SEC
        while True:
            ft817_0.read_frequency()
            ft817_0.read_rx_status()
            ft817_1.read_frequency()
            ft817_1.read_rx_status()
            print
            print ("TX: " + str(ft817_0))
            print
            print ("RX: " + str(ft817_1))
            down = str(ft817_1)[0:8]
            down_int = int(down)
            up_int = down_int - 28950000
            up_float = up_int / 100.0
            down_10g = (down_int + 1005580000) / 100.0
            print ("Up INT: " + str(up_float))
            print ("Down INT: " + str(down_10g))
            up = str(up_int)
            ft817_0.set_tx(up)
            lcd.message = (str(down_10g) +"\n" + down[3:8] + "/" +  up[3:8])
    except KeyboardInterrupt:
        # KeyboardInterrupt exception is thrown when CTRL-C or CTRL-Break is pressed. 
        pass
    except Exception as e:
        print ("\r\nError has occured. Error message:")
        print (str(e))
        print ("\r\n")
    finally:
        print ("See you later. 73!")
