import socket
import PySimpleGUIQt as sg
import sys
import os


try:
   wd = sys._MEIPASS
except AttributeError:
   wd = os.getcwd()
file_path = os.path.join(wd, 'icon.ico')


def hostnameOnTray():
    menu = ['', ['Exit']]
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    tooltip = hostname + ' ' + ip
    tray = sg.SystemTray(menu=menu, filename=file_path, tooltip=tooltip)

    while True:
        menu_item = tray.Read()
        if menu_item == 'Exit':
            break


if __name__ == '__main__':
    hostnameOnTray()
