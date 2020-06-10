from flask import Flask, jsonify, request, make_response
from pyDTS.endpoint import BaseEndpoint


app = Flask(__name__)
# app.config["DEBUG"] = True

__endpoint = BaseEndpoint()
__endpoint_path = __endpoint.endpoint_path
print(__endpoint_path)


def set_host(host_path):
    __endpoint.host_prefix = host_path

# TODO: handle request parameters
# TODO: handle GET, POST, etc. separately


@app.route("/")
def home():
    # ony GET allowed
    entry = "" + request.base_url + __endpoint_path
    entry = entry.replace("//", "/")
    return f"<h1>DTS Mimicker</h1>" \
           f"<div>Visit <a href=\"{__endpoint_path}\">the Base API Endpoint</a> " \
           f"at <a href=\"{__endpoint_path}\">{entry}</a> " \
           f"for DTS functionality.</div>"


@app.route(__endpoint_path)
def entry_point():
    # ony GET allowed
    return make_response(jsonify(__endpoint.entrypoint_response), 200)


@app.route(__endpoint.collections_path)
def collections():
    # ony GET allowed
    return make_response(jsonify(__endpoint.collections_response), 200)


class DTSMServer:
    """DTS Mimicker Server.

    A server that mimics the behavior of a "real" DTS server.
    Intended for test purposes etc.
    """

    def __init__(self, host, port):
        """`dtsmserver` constructor.

        Generates an instance of `dtsmserver`.

        Args:
            host (str): the host prefix (e.g. "localhost" or "127.0.0.1")
            port (int): the port to run on
        """
        print("Initializing Server")
        super().__init__()
        self.host = host
        self.port = port
        set_host(f"http://{host}:{port}")

    def run(self):
        """Run method.

        Run the server.
        """
        print("Running flask server")
        app.run(host=self.host, port=self.port)
