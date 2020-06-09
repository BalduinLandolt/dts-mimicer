from flask import Flask

class DTSM_server():
    """DTS Mimicer Server
    """

    def __init__(self, port):
        print("Initializing Server")
        super().__init__()
        self.port = port

    def run(self):
        pass