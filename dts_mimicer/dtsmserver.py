from flask import Flask, jsonify, request, make_response

from pyDTS.constants import CollectionsConstants
from pyDTS.endpoint import BaseEndpoint

app = Flask(__name__)
# app.config["DEBUG"] = True

__endpoint = BaseEndpoint()
__endpoint_path = __endpoint.endpoint_path
print(__endpoint_path)


def set_host(host_path):
    __endpoint.host_prefix = host_path

# QUESTION: handle GET, POST, etc. separately?


@app.route("/")
def home():
    # ony GET allowed
    entry = "" + request.base_url + __endpoint_path
    entry = entry.replace("//", "/")

    epc = __endpoint.collections_path
    qm = "?"
    et = "&"
    nav_parent = "nav=parent"
    id_01 = "id=sample_01"
    pg_01 = "page=1"
    return f"<h1>DTS Mimicker</h1>" \
           f"<div>Visit <a href=\"{__endpoint_path}\">the Base API Endpoint</a> " \
           f"at <a href=\"{__endpoint_path}\">{entry}</a> " \
           f"for DTS functionality.</div>" \
           f"<h4>Sample Queries:</h4><div>" \
           f"<p>Click on one of the following Links</p><ul>" \
           f"<li><a href=\"{epc}\">{epc}</a></li>" \
           f"<li><a href=\"{epc+qm+id_01}\">{epc+qm+id_01}</a></li>" \
           f"<li><a href=\"{epc+qm+id_01+et+nav_parent}\">{epc+qm+id_01+et+nav_parent}</a></li>" \
           f"<li><a href=\"{epc+qm+id_01+et+pg_01}\">{epc+qm+id_01+et+pg_01}</a></li>" \
           f"</ul></div>"


@app.route(__endpoint_path)
def entry_point():
    # ony GET allowed
    return make_response(jsonify(__endpoint.entrypoint_response), 200)


@app.route(__endpoint.collections_path)
def collections():
    # ony GET allowed
    id_arg = None
    if "id" in request.args:
        id_arg = request.args["id"]
    page_arg = None
    if "page" in request.args:
        page_arg = request.args["page"]
    nav_arg = CollectionsConstants.NAV_CHILDREN
    if "nav" in request.args:
        nav_arg = request.args["nav"]
    return make_response(jsonify(__endpoint.get_collections_response(id=id_arg, page=page_arg, nav=nav_arg)), 200)


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
