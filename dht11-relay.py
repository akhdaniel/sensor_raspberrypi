import Adafruit_DHT
import time
import odoorpc
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode


odoo = odoorpc.ODOO('iot.vitraining.com', port=8069)
odoo.login('iot', 'admin', 'v1tr41n1ng com')
reading = odoo.env['vit.reading']

def turn_on():
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # out

def turn_off():
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # on
try:
        while True:
                humidity, temp = Adafruit_DHT.read_retry(11, 4)
                print("Humidity=%s, Temp=%s" % (humidity, temp) )
                if temp >= 27:
                        turn_on()
                else:
                        turn_off()

                reading.create({
                'read_date': time.strftime("%Y-%m-%d %H:%M:%S"),
                'humidity' : humidity,
                'temperature' : temp,
                'sensor_id': 1
                })
except:
        GPIO.cleanup()
        