#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
 
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
        self.send_response(200)
 
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        message = "Hello world!"
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
  print('-> Starting server...')
 
  server_address = ('', 8080)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('-> Running server in port 8080')
  httpd.serve_forever()
 
run()
