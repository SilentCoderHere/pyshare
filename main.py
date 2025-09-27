import sys

from file_transfer.receiver import startReceiver
from file_transfer.sender import startSender


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [sender|receiver] [options]")
        return

    mode = sys.argv[1].lower()

    if mode == "sender":
        if len(sys.argv) < 3:
            print("Usage: python main.py sender <filename>")
            return
        filename = sys.argv[2]
        startSender(filename)

    elif mode == "receiver":
        host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"
        port = int(sys.argv[3]) if len(sys.argv) > 3 else 8000
        startReceiver(host, port)

    else:
        print("Invalid option. Use 'sender' or 'receiver'.")


if __name__ == "__main__":
    main()
