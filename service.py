from flask import Flask, jsonify, request
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

@app.route("/pins", methods=["POST"])
def set_pins():
    for k, v in request.get_json().items():
        GPIO.setup(int(k), GPIO.OUT)
        if v == "false" or False:
            GPIO.output(int(k), GPIO.LOW)
        else:
            GPIO.output(int(k), GPIO.HIGH)
    
    return jsonify({"status":"ok"})

