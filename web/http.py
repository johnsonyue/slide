import time
import json
import os
import BaseHTTPServer
import cgi

class Server(BaseHTTPServer.HTTPServer):
	def __init__(self, (HOST_NAME, PORT_NUMBER), handler):
		BaseHTTPServer.HTTPServer.__init__(self, (HOST_NAME, PORT_NUMBER), handler)
	
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
	def do_GET(self):
		"""Respond to a GET request."""
		path = self.path.split('/')[-1]
		path = path.replace('/','')
		if (os.path.exists(path)):
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(open(path,'r').read())
		else:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write("404 NOT FOUND")
