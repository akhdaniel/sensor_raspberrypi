import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
import odoorpc
odoo = odoorpc.ODOO('iot.vitraining.com', port=8069)
odoo.login('db_name', 'user', 'passwd')
reading = odoo.env['vit.reading']

while True:
	temperature = sensor.get_temperature()
	print("The temperature is %s celsius" % temperature)
	reading.create({
		'read_date': time.strftime("%Y-%m-%d %H:%M:%S"),
		'sensor_id': 1,
		'temperature': temperature
		})
	time.sleep(5)

