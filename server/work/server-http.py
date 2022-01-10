import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import json

class Server(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/gpt':
            # We are sending a JSON file
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # get the input prompt
            # send out the json file
            self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))
            return
            
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
ADDRESS = ""
PORT = 8000
handler_object = Server
serverInstance = socketserver.TCPServer((ADDRESS, PORT), handler_object)
serverInstance.serve_forever()
