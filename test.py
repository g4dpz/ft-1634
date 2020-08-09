from ft817 import FT817
import time

# Constants
SERIAL_PORT0 = "/dev/ttyUSB0"
SERIAL_PORT1 = "/dev/ttyUSB1"
SAMPLES_PER_SEC = 5

if __name__ == '__main__':
    print ("Starting FT-817ND monitor...")
    
    try:
        ft817_0 = FT817(SERIAL_PORT0)
        ft817_1 = FT817(SERIAL_PORT1)
        delay = 1.0 / SAMPLES_PER_SEC
        while True:
            ft817_0.read_frequency()
            ft817_0.read_rx_status()
            ft817_1.read_frequency()
            ft817_1.read_rx_status()
            print
            print (ft817_0)
            print
            print (ft817_1)
            time.sleep(delay)
    except KeyboardInterrupt:
        # KeyboardInterrupt exception is thrown when CTRL-C or CTRL-Break is pressed. 
        pass
    except Exception as e:
        print ("\r\nError has occured. Error message:")
        print (str(e))
        print ("\r\n")
    finally:
        print ("See you later. 73!")
