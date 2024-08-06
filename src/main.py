from http.server import HTTPServer, BaseHTTPRequestHandler
from prometheus_client import start_http_server, Counter, GC_COLLECTOR, PLATFORM_COLLECTOR, PROCESS_COLLECTOR, REGISTRY
import json

# Service Config
HTTP_ADDRESS = "0.0.0.0"
HTTP_PORT = 8000

# Prometeheus Conig
PROM_PORT = 8080
METRIC_NAME = "http_foxes_count"

instance_counter = Counter(METRIC_NAME, "Foxes instance count")


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            foxes_json = {
                "components":
                    {"foxes":
                            {"count": instance_counter._value.get()}
                        }
            }
            
            output = json.dumps(foxes_json).encode()
            self.wfile.write(output)
        
        elif self.path == "/plusone":
            instance_counter.inc()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hi, fox! Fox counter increased by one")
        
        elif self.path == "/reset":
            instance_counter._value.set(0)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Fox counter reseted")
        
        else:
            self.send_response(404)
            self.end_headers()


def main():
    REGISTRY.unregister(GC_COLLECTOR)
    REGISTRY.unregister(PLATFORM_COLLECTOR)
    REGISTRY.unregister(PROCESS_COLLECTOR)
    start_http_server(PROM_PORT)

    httpd = HTTPServer((HTTP_ADDRESS, HTTP_PORT), SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
