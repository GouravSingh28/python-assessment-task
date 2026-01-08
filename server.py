from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class AckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {
            "status": "ACK",
            "message": "GET request received"
        }

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {
            "status": "ACK",
            "message": "POST request received"
        }

        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0", 80), AckHandler)
print("Server running on port 80...")
server.serve_forever()
