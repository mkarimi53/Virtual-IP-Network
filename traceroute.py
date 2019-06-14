import socket, threading,sys
from node_info import Link_info,Node_info
from IP import IPPacket
from link_layer import LinkLayer


class TraceRoute:
    def __init__(self,linklayer,nodeInfo):
        self.linklayer=linklayer
        self.nodeInfo=nodeInfo
    def run():
        self.currentTTL=1
        self.path=[]
        
        self.linklayer.sendData()