
# -*- coding: utf-8 -*-

import ruamel.yaml
import socket
import sys
import ftplib
import subprocess
import ifaddr
from analyse import analyse

port1 = 3142
ftp = ftplib.FTP()
x = 0
yaml = ruamel.yaml.YAML()

with open("oini.yaml") as iniFile:
    yamlF = yaml.load(iniFile)

print ("server load")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", port1))
while True:
    try:
        buf = sock.recv(1024).decode()
        print ("tm: ", buf)
        d = buf.split(',')
        if 'analyse' in d[0]:
            listsys = [d[i+1][2:-1] for i in range(11)]
            print(listsys[x])
            host = d[12]
            port = d[13]
            while x != 10:
                yamlF["LoadList"][0] = listsys[x]
                with open("ini.yaml","w") as outFile:
                    yaml.dump(yamlF, outFile)
                Popen('python main.pyw', creationflags=CREATE_NEW_CONSOLE)
                analyse.analyse()
                x += 1
            yamlF["LoadList"] = listsys
            with open("ini.yaml","w") as iniFile:
                yaml.dump(yamlF, iniFile)
            print('Sending answer...')
            ftp.connect(eval(host), int(port))
            ftp.login("root", "root")
            ans = open("answer.txt", "r")
            ftp.storbinary("STOR answer.txt", ans)
    except:
        a = 1
