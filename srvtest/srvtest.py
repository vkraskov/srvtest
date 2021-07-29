from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

USE_HTTPS = False

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message =  threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    server = ThreadingSimpleServer(('0.0.0.0', 4444), Handler)
    if USE_HTTPS:
        import ssl
        #server.socket = ssl.wrap_socket(server.socket, keyfile='./key.pem', certfile='./cert.pem', server_side=True)
        server.socket = ssl.wrap_socket(server.socket, server_side=True)
    server.serve_forever()

if __name__ == '__main__':
	run()
    
