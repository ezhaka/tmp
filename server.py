#!/usr/bin/env python3
"""
Simple HTTP server that responds "I'm okay" on the root path.
Runs on port 3000.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import sys


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Respond with "I'm okay" for root path
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"I'm okay")
        else:
            # Return 404 for any other path
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Not Found")

    def log_message(self, format, *args):
        # Log messages to stdout
        print(f"[{self.log_date_time_string()}] {format % args}")


def run_server(port=3000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Starting server on port {port}...")
    print(f"Server running at http://localhost:{port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()


if __name__ == '__main__':
    run_server()