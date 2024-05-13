from threading import Thread,Event
from time import sleep
# from iams_can import *
import webServer



if __name__ == '__main__':
    webServer.runWebServer(debug=False, host="0.0.0.0")