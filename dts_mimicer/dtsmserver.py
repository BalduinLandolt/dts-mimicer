from flask import Flask, jsonify
from pyDTS.endpoint import BaseEndpoint


app = Flask(__name__)
# app.config["DEBUG"] = True

_endpoint = BaseEndpoint()
_endpoint_path = _endpoint.endpoint_path
print(_endpoint_path)


@app.route("/")
def home():
    return f"<h1>DTS Mimicker</h1>" \
           f"<div>Visit <a href=\"{_endpoint_path}\">the Base API Endpoint at {_endpoint_path}</a> " \
           f"for DTS functionality.</div>"


@app.route(_endpoint_path)
def entry_point():
    return jsonify(_endpoint.reply)


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
