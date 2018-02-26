#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from handler import handler

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        length = int(self.headers['content-length'])
        data = self.rfile.read(length)
        self.wfile.write(handler(data))

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting http server...')
    httpd.serve_forever()

if __name__ == "__main__":
    print('starting...')
    run(port=8080)
