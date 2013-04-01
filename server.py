#!/usr/bin/python

import string, cgi, time, os
from os import fork, chdir, setsid, umask
from sys import exit
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import RPi.GPIO as io
io.setmode(io.BCM)

in1_pin = 4
in2_pin = 17
in3_pin = 23
in4_pin = 24

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)
speed = int(9) * 11

# Turn light on
io.setup(22, io.OUT)
io.output(22, True)

def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()
    except:
        print("Error writing to: " + property + " value: " + value)

set("delayed", "0")
set("mode", "pwm")
set("frequency", "10")
set("active", "1")

def backward():
    set("duty", str(speed))
    io.output(in1_pin, False)
    io.output(in2_pin, True)
    io.output(in3_pin, False)
    io.output(in4_pin, True)

def forward():
    set("duty", str(speed))
    io.output(in1_pin, True)
    io.output(in2_pin, False)
    io.output(in3_pin, True)
    io.output(in4_pin, False)

def left():
    set("duty", str(11))
    io.output(in1_pin, True)
    io.output(in2_pin, False)
    io.output(in3_pin, False)
    io.output(in4_pin, True)

def right():
    set("duty", str(11))
    io.output(in1_pin, False)
    io.output(in2_pin, True)
    io.output(in3_pin, True)
    io.output(in4_pin, False)

def stop():
    io.output(in1_pin, False)
    io.output(in2_pin, False)
    io.output(in3_pin, False)
    io.output(in4_pin, False)


import time
import urllib2

set("duty", str(speed))
 
class MyRequestHandler(BaseHTTPRequestHandler):

	def address_string(self):
		return str(self.client_address[0])

	def do_GET(self):
		try:
			urlpath = self.path
			action, dump = urlpath.split("?",2)
			if action == "/forward" or action == "/backward" or action == "/left" or action == "/right" or action == "/stop":
				self.send_response(200)
				self.send_header("Content-type", "text/javascript")
				self.end_headers()
				if action == "/forward":
					forward()
					self.wfile.write("ok")
				elif action == "/backward":
					backward()
					self.wfile.write("ok")
				elif action == "/left":
					left()
					self.wfile.write("ok")
				elif action == "/right":
					right()
					self.wfile.write("ok")
				elif action == "/stop":
					stop()
					self.wfile.write("ok")
				else:
					self.wfile.write("Eeek, we have an issue")
			else:
				self.send_error(404, "File not found %s" % self.path)
		except:
			self.send_error(404, "File not found %s" % self.path)

def main():
	try:
		server = HTTPServer(("",8090), MyRequestHandler)
		print "Starting httpserver..."
		server.serve_forever()
	except KeyboardInterrupt:
		print "^C received, shutting down server"
		server.socket.close()

if __name__ == "__main__":
	main()
