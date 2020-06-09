from flask import Flask


app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route("/")
def home():
    return "Hello World"

class DTSM_server():
    """DTS Mimicer Server
    """

    def __init__(self, port):
        print("Initializing Server")
        super().__init__()
        self.port = port

    def run(self):
        print("Running flask server")
        app.run(port=self.port)
