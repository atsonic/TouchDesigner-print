import os
import time
import sys
import socket
from argparse import ArgumentParser

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyWatchHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_any_event(self, event):
        pass

    def on_created(self, event):
        sendUDP(os.path.basename(event.src_path))


def msg_to_bytes(msg):
    return str(msg).encode('utf-8')

def sendUDP(basename):
    upd_ip = "127.0.0.1"
    udp_port = int(7000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg_to_bytes(basename), (upd_ip, udp_port))

def monitor():
    event_handler = MyWatchHandler()
    observer = Observer()
    observer.schedule(event_handler, '../images/', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def main():
    monitor()


if __name__ == "__main__":
    main()