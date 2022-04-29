import sys
import http.server
import socketserver
import subprocess

class httpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/date", "/%H:%M:%S"]:
            self.path = "static" + self.path + ".html"
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == "/":
            self.path = "static/index.html"
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
<meta http-equiv="autorefresh" content="1" /> 

conf = subprocess.run(["grep", "port = 8000", "/var/tmp/mytime/mytime.conf"], stdout = subprocess.PIPE)
if b" = " not in conf.stdout:
    print("Could not read configuration file `/var/tmp/mytime/mytime.conf`")
    sys.exit(1)
port = conf.stdout.split(b" = ")[1]

socketserver.TCPServer.allow_reuse_address = True
server = socketserver.TCPServer(("", int(port)), httpRequestHandler)
server.serve_forever()
