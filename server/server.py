'''
	call the api with : http://localhost:8000/ask;'Dear Sir,'
'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from urllib.parse import urlparse

import gpt_2_simple as gpt2
import tensorflow as tf

sess = gpt2.start_tf_sess(threads=1)
gpt2.load_gpt2(sess)

print("Ready")

def speak_with_prefix(prefix):
	res = gpt2.generate(sess,
						length=100,
						temperature=0.7,
						prefix=prefix,
						nsamples=1,
						batch_size=1,
						return_as_list=True
						)[0]
	return res;

class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		parsed = urlparse(self.path)
		if parsed.path == '/ask':
			parameter = parsed.params
			parameter = parameter.strip("'")
			parameter = urllib.parse.unquote(parameter)
			print(parameter)
			self.send_response(200)
			self.send_header('Content-type','text/plain')
			self.send_header('Access-Control-Allow-Origin', '*')
			self.end_headers()

			message = speak_with_prefix(parameter)
			#message = "test"
			self.wfile.write(bytes(message, "utf8"))
		
		
		
		else:
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(bytes("bad request", "utf8"))

with HTTPServer(('', 8000), handler) as server:
	server.serve_forever()
	