import argparse


def start():
    parser = argparse.ArgumentParser(usage="DTS Mimicer.\nBy default, run server; for client, use flag.")
    parser.add_argument("-c","--client", help="run client", action="store_true")
    args = parser.parse_args()
    if args.client:
        print("Starting Client...")
        # TODO: start client
    else:
        print("Starting Server...")
        # TODO: start server


if __name__ == "__main__":
    start()
