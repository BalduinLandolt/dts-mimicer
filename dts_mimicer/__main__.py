import argparse
from dtsm_server import DTSM_server


def start():
    parser = argparse.ArgumentParser(usage="DTS Mimicer.\nBy default, run server; for client, use flag.\nDefault port: 17980")
    parser.add_argument("-c","--client", help="run client", action="store_true")
    parser.add_argument("-p","--port", help="the port to run on", type=int, default=17980)
    args = parser.parse_args()
    port = args.port
    if args.client:
        print(f"Starting Client on Port {port}...")
        # TODO: start client
    else:
        print(f"Starting Server on Port {args.port}...")
        server = DTSM_server(port)
        server.run()
        # TODO: start server


if __name__ == "__main__":
    start()
