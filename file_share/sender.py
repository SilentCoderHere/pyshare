from os import path, stat
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from time import sleep
from typing import Optional

from file_share.utils.animation import Animation
from file_share.utils.ip import getIPAddress
from file_share.utils.sizeformatter import sizeFormat


class Sender(Thread):
    def __init__(self, filename: str, length: int):
        super().__init__()
        self.length = length
        self.byteSent = 0
        self.filename = filename
        self.client: Optional[socket] = None

    def setClient(self, client):
        self.client = client

    def run(self):
        with open(self.filename, "rb") as file:
            for filedata in file.readlines():
                if self.client is None:
                    break
                self.client.send(filedata)
                self.byteSent += len(filedata)


def startSender(filename: str, port: int = 8000):
    if not path.exists(filename):
        print(f"\n\n{filename!r} File Not Found!")
        return

    fileLength = stat(filename).st_size
    fileSize = sizeFormat(fileLength, 1)
    host = getIPAddress()

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)

    print(f"\nServer started on ({host}, {port})")

    anim = Animation("Waiting", 0.3)
    anim.start()

    client, address = sock.accept()
    anim.stop()

    print("Receiver Connected!")

    client.send(f"{path.basename(filename)}!!{fileLength}".encode())
    client.recv(1024)  # response ignored

    print(f"SENDING: {filename!r}\n")

    sender = Sender(filename, fileLength)
    sender.setClient(client)
    sender.start()

    sleep(0.2)

    while True:
        byte = sender.byteSent
        percent = round(byte / fileLength * 100, 1)
        print(f"\r{percent}% {sizeFormat(byte, 1)}/{fileSize}")
        print("\033[F", end="\033[K")

        if byte >= fileLength:
            break
        sleep(0.1)

    client.send(b"File Sent")
    sock.close()
    print("File Sent Successfully")
