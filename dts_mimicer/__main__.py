import argparse
from dtsmserver import DTSMServer


def start():
    parser = argparse.ArgumentParser(usage="DTS Mimicker.\n"
                                           "By default, run server; for client, use flag.\n"
                                           "Default host: localhost\n"
                                           "Default port: 17980\n\n")
    parser.add_argument("-c", "--client", help="run client", action="store_true")
    parser.add_argument("-p", "--port", help="the port to run on", type=int, default=17980)
    parser.add_argument("-ho", "--host", help="the host to run on", type=str, default="localhost")
    args = parser.parse_args()
    host = args.host
    port = args.port
    if args.client:
        print(f"Starting Client on Port {port}...")
        # TODO: start client
    else:
        print(f"Starting Server on Port {args.port}...")
        server = DTSMServer(host, port)
        server.run()


if __name__ == "__main__":
    start()
