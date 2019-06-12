import socket, threading,sys,selectors
from node_info import Link_info,Node_info
from IP import IPPacket
from link_layer import LinkLayer


class TraceRoute:
    def __init(self,linklayer,nodeInfo):
        self.linklayer=linklayer
        self.nodeInfo=nodeInfo
        self.currentTTL=1
        self.graph=[]
        self.reachedInterfaces=[]
        for x in self.nodeInfo.remote:
            self.graph.append()
    def run(self):
        