from flask import Flask, jsonify, request
from pyDTS.endpoint import BaseEndpoint


app = Flask(__name__)
# app.config["DEBUG"] = True

__endpoint = BaseEndpoint()
__endpoint_path = __endpoint.endpoint_path
print(__endpoint_path)


@app.route("/")
def home():
    print(request.base_url)
    return f"<h1>DTS Mimicker</h1>" \
           f"<div>Visit <a href=\"{__endpoint_path}\">the Base API Endpoint at {__endpoint_path}</a> " \
           f"for DTS functionality.</div>"


@app.route(__endpoint_path)
def entry_point():
    return jsonify(__endpoint.entrypoint_reply)


@app.route(__endpoint.collections_path)
def collections():
    return jsonify(__endpoint.collections_reply)


class DTSMServer:
    """DTS Mimicker Server
    """

    def __init__(self, port):
        print("Initializing Server")
        super().__init__()
        self.port = port

    def run(self):
        print("Running flask server")
        app.run(port=self.port)
