import Adafruit_DHT
import time
import odoorpc

odoo = odoorpc.ODOO('iot.vitraining.com', port=8069)
odoo.login('db_name', 'user', 'passwd')
reading = odoo.env['vit.reading']

while True:
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
	reading.create({
		'read_date': time.strftime("%Y-%m-%d %H:%M:%S"),
		'sensor_id': 1,
		'temperature': temperature,
		'humidity': humidity
		})
	time.sleep(5)

