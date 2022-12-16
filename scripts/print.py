import time
import sys
import socket
from argparse import ArgumentParser
import win32con
import win32print
import win32ui
from PIL import Image, ImageWin
 
def msg_to_bytes(msg):
    return str(msg).encode('utf-8')

def print(port, file):
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 110

    printer_name = win32print.GetDefaultPrinter ()

    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)

    bmp = Image.open (file)

    hDC.StartDoc (file)
    hDC.StartPage ()

    dib = ImageWin.Dib (bmp)
    dib.draw (hDC.GetHandleOutput (), (0,0,printer_size[0],printer_size[1]))

    hDC.EndPage ()
    hDC.EndDoc ()
    hDC.DeleteDC ()
    callbackFunc(port)

def callbackFunc(port):
    upd_ip = "127.0.0.1"
    udp_port = int(args.port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg_to_bytes('success'), (upd_ip, udp_port))

if __name__ == '__main__':
    parser = ArgumentParser(description='Print')
    parser.add_argument("-p", "--port", dest="port", help="UDP port", required=True, default=1234)
    parser.add_argument("-f", "--file", dest="file", help="file", required=True, default=1234)
    args = parser.parse_args()
    print(args.port, args.file)
    pass