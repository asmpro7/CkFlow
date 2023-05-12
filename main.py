# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))
import speedtest
import urllib.request
import math
from flowlauncher import FlowLauncher

def byt_to_mb(bytes):
    x=int(math.floor(math.log(bytes,1024)))
    power=math.pow(1024,x)
    size=round(bytes/power,2)
    return f"{size} Mpbs"

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

class CkFlow(FlowLauncher):

    def query(self, query):
        output=[]
        
        try:
            if connect():
                if query=="s":     
                    speed=speedtest.Speedtest()
                    download=speed.download()
                    output.append({"Title": f"Download speed: {byt_to_mb(download)}","IcoPath": "Images/down.png"})
                    upload=speed.upload()
                    output.append({"Title": f"Upload speed: {byt_to_mb(upload)}","IcoPath": "Images/up.png"})
                elif query=="d":
                    speed=speedtest.Speedtest()
                    download=speed.download()
                    output.append({"Title": f"Download speed: {byt_to_mb(download)}","IcoPath": "Images/down.png"})
                elif query=="u":
                    speed=speedtest.Speedtest()
                    upload=speed.upload()
                    output.append({"Title": f"Upload speed: {byt_to_mb(upload)}","IcoPath": "Images/up.png"})
                else:
                    output.append({"Title": "Connected !","IcoPath": "Images/cont.png"})
                
            else:
                output.append({"Title": "No internet access !","IcoPath": "Images/conn.png"})
        except:
            output.append({"Title": "No internet access !","IcoPath": "Images/conn.png"})
        return output
if __name__ == "__main__":
    CkFlow()
