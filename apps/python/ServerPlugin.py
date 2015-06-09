__author__ = 'Scott Davey'

"""Simple tyre temperature plugin for Assetto Corsa"""
import sys
import ac
import acsys
import traceback
sys.path.insert(0, 'apps/python/ServerPlugin/ServerPlugin_lib/stdlib')
try:
    import socketserver
    import threading
    from ServerPlugin_lib.UDPServer import UDPServer
except Exception as e:
    ac.log("{}".format(traceback.format_exc()))

APP_NAME = "ACServer"
statusLabel = 0
server = None

def log(txt):
    ac.log("ACServer: " + txt)

def acMain(ac_version):
    global server
    try:
        appWindow = ac.newApp(APP_NAME)
        ac.setSize(appWindow, 200, 200)
        server = socketserver.UDPServer(('localhost', 18149), UDPServer)
        threading.Thread(target=server.serve_forever).start()
        setupUI(appWindow)
        log("Startup Complete")
    except Exception as e:
        log("ERROR:  {}".format(e))
    return APP_NAME

def setupUI(appWindow):
    global statusLabel
    statusLabel = ac.addLabel(appWindow, "Disconnected");
    ac.setFontColor(statusLabel, 255, 0, 0, 0)
    ac.setPosition(statusLabel, 3, 30)

def acShutdown():
    global server
    server.shutdown()

