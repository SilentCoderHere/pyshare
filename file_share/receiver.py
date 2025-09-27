from os import path
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from time import sleep, time

from file_share.utils.sizeformatter import sizeFormat


class Receiver(Thread):
    def __init__(self, filename: str, length: int, sock: socket):
        super().__init__()
        self.length = length
        self.byteReceived = 0
        self.filename = filename
        self.sock = sock

    def run(self):
        with open(self.filename, "ab") as file:
            while True:
                data = self.sock.recv(1024)
                if data.endswith(b"File Sent"):
                    break
                self.byteReceived += file.write(data)


def startReceiver(host: str = "127.0.0.1", port: int = 8000):
    sock = socket(AF_INET, SOCK_STREAM)

    try:
        sock.connect((host, port))
    except Exception as e:
        print(e)
        print(f"Can't connect to ({host}, {port})")
        return

    fileData = sock.recv(1024).decode().split("!!")
    fileLength = int(fileData[1])
    filename = fileData[0]
    fileSize = sizeFormat(fileLength, 1)

    if path.exists(filename):
        date = str(int(time()))
        parts = filename.split(".")
        if len(parts) > 1:
            filename = f"{parts[0]}_{date}.{parts[1]}"
        else:
            filename = f"{filename}_{date}"

    sock.send(b"DATASENT\r\n")

    print(f"RECEIVING: {filename!r}\n")

    receiver = Receiver(filename, fileLength, sock)
    receiver.start()

    sleep(0.2)

    while True:
        byte = receiver.byteReceived
        percent = round(byte / fileLength * 100, 1)
        print(f"\r{percent}% {sizeFormat(byte, 1)}/{fileSize}")
        print("\033[F", end="\033[K")

        if byte >= fileLength:
            break
        sleep(0.1)

    print("File Received Successfully!")
