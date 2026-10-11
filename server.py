"""
THE BLUEBOP CAFE & BAR — LOCAL DEVELOPMENT SERVER
Supports HTTP 206 Partial Content (Range Requests) for smooth video scrubbing on mobile & desktop browsers.
"""

import os
import sys
import re
from http.server import HTTPServer, SimpleHTTPRequestHandler

class RangeFileWrapper:
    def __init__(self, fp, length):
        self.fp = fp
        self.remaining = length

    def read(self, size=-1):
        if self.remaining <= 0:
            return b''
        to_read = size if (size > 0 and size < self.remaining) else self.remaining
        data = self.fp.read(to_read)
        self.remaining -= len(data)
        return data

    def close(self):
        self.fp.close()


class RangeRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def send_head(self):
        if 'Range' not in self.headers:
            return super().send_head()

        path = self.translate_path(self.path)
        if not os.path.isfile(path):
            return super().send_head()

        f = None
        try:
            f = open(path, 'rb')
            fs = os.fstat(f.fileno())
            total_length = fs[6]

            range_header = self.headers.get('Range')
            m = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if not m:
                f.close()
                return super().send_head()

            start = int(m.group(1))
            end = int(m.group(2)) if m.group(2) else total_length - 1
            if start >= total_length:
                f.close()
                self.send_error(416, "Requested Range Not Satisfiable")
                return None

            end = min(end, total_length - 1)
            content_length = end - start + 1

            self.send_response(206)
            self.send_header('Content-Type', self.guess_type(path))
            self.send_header('Content-Range', f'bytes {start}-{end}/{total_length}')
            self.send_header('Content-Length', str(content_length))
            self.end_headers()

            f.seek(start)
            return RangeFileWrapper(f, content_length)
        except Exception:
            if f:
                f.close()
            return super().send_head()


def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RangeRequestHandler)
    print(f"===========================================================")
    print(f" THE BLUEBOP CAFE & BAR — WEB SERVER RUNNING")
    print(f" URL: http://localhost:{port}/")
    print(f" Serving directory: {os.getcwd()}")
    print(f" Video scrub Range requests enabled.")
    print(f"===========================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run_server(port)
