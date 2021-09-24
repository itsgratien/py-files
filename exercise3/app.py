from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"

port = 800


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, 'it is working')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write('Hello world'.encode())


if __name__ == "__main__":
    webserver = HTTPServer(('', port), Server)
    try:
        webserver.serve_forever()
        print("server started")
    except KeyboardInterrupt:
        pass
    webserver.server_close()
