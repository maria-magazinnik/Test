from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 9500


class RequestHandler(BaseHTTPRequestHandler):
    def payload(self):
        payload_size = int(self.headers['Content-Length'])
        payload = self.rfile.read(payload_size)
        return payload

    def set_headers(self):
        self.send_response(200, "OK")
        self.end_headers()

    def do_POST(self):
        payload = self.payload()
        self.set_headers()
        self.wfile.write("POST: {}".format(payload).encode('utf-8'))

    def do_GET(self):
        payload = self.payload()
        self.set_headers()
        self.wfile.write("GET: {}".format(payload).encode('utf-8'))

    def do_PUT(self):
        payload = self.payload()
        self.set_headers()
        self.wfile.write("PUT: {}".format(payload).encode('utf-8'))

    def do_DELETE(self):
        payload = self.payload()
        self.set_headers()
        self.wfile.write("DELETE: {}".format(payload).encode('utf-8'))


def run_server():
    server = HTTPServer(('', PORT), RequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    run_server()
