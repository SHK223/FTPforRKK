from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import ruamel.yaml
import socket
import sys
import os
from os import path
import logging

class MyHandler(FTPHandler):

    def on_connect(self):
        print ("%s:%s connected" % self.addr)

    def on_disconnect(self):
        pass

    def on_login(self, username):
        pass

    def on_logout(self, username):
        pass

    def on_file_sent(self, file):
        pass

    def on_file_received(self, file):
        print("received" + ' ' + file)

    def on_incomplete_file_sent(self, file):
        pass

    def on_incomplete_file_received(self, file):
        os.remove(file)

yaml = ruamel.yaml.YAML()
host ="127.0.0.1"
port = 7777
with open("oini.yaml") as iniFile:
    yamlF = yaml.load(iniFile)

def main():
    authorizer = DummyAuthorizer()
    listsys = []

    for sysId in yamlF["LoadList"]:
        listsys.append(sysId)
        FTP_User = yamlF[sysId]["Login"]
        FTP_Ip = yamlF[sysId]["Ip"]
        FTP_Port = yamlF[sysId]["Port"]
        FTP_Password = yamlF[sysId]["Password"]
        FTP_Directory = os.path.abspath(os.getcwd())
        authorizer.add_user(FTP_User, FTP_Password, FTP_Directory, perm='elradfmw', msg_login="Login successful")

    handler = MyHandler
    handler.authorizer = authorizer

    if not path.exists("C:/log/pyftpd.log"):
        os.makedirs("C:/log/")
    logging.basicConfig(filename='/log/pyftpd.log', level=logging.DEBUG)

    handler.banner = "pyftpdlib based ftpd ready."

    address = (host, port)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("127.0.0.1", 3142))
    while True:
        try:
            buf = input(">>")
            s.send(buf.encode())
            if buf == "run":
                ef = ['C:\\Учеба\\payloadDownloader\\multiThread\\analyse.py', listsys, host, port]
                d = str(ef)[1:-1]
                s.send(d.encode())
                break
        except:
            a = 1


    server.serve_forever()


if __name__ == '__main__':
    main()
