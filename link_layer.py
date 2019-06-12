import socket, threading,sys,selectors
from node_info import Link_info,Node_info
from IP import IPPacket
from traceroute import TraceRoute
class LinkLayer:
    DataLoadLimit=1400
    #un baba 64KB chi mige ???
    def __init__(self,port,bufferSize):
        self.localPort=port
        self.localIP="127.0.0.1"
        self.bufferSize=bufferSize
        self.UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)       
        self.UDPSocket.bind((self.localIP, self.localPort)
        self.recieving=True
    
    
    def sendData(self,port,data):
        self.UDPSocket.sendto(data, (self.localIP,port))
    
    def recievingData(self):
        while(self.recieving):
            try:
                msgFromServer = self.UDPSocket.recvfrom(self.bufferSize)
            except socket.error as r:
                print("i got error",r)
            print(msgFromServer[0].decode())

 
class Node:
    def  __init__(self,filePath):     
        self.commandList=["interfaces","routes","down","up","send","q","traceroute"]
        self.node_info=Node_info(filePath)
        self.lk=LinkLayer(self.node_info.lport,100)

    def sendIPMessageToDst(self,dstIP,message):
        #
        ippacket=IP()
         #find interface and next node from routing table 
        #ippacket.assignValues(dataLength,id,fragFlag,fragOffset,src,dst,protocol,ttl,ICMPtype,irfh,packet)
        #self.lk.sendData(next node port,ippacket.packIPv4())           

    def run(self):
        while(True):
            commandraw=input(">")
            command=commandraw.split(" ")
            if(command[0]==self.commandList[0]):#interfaces
                for x in self.node_info.remotes:
                    print(x.remote_host,x.remote_port,x.local_virt_ip,x.remote_virt_ip)
            elif(command[0]==self.commandList[1]):#routes
                print(self.commandList[1])
            elif(command[0]==self.commandList[2]):#downsen
                print(self.commandList[2])
            elif(command[0]==self.commandList[3]):#up
                print(self.commandList[3])
            elif(command[0]==self.commandList[4]):#send
                interfaceNum=int(command[1])
                self.sendIPMessageToDst(self,dstIP,command[2])
                print(self.commandList[4])
            elif(command[0]==self.commandList[5]):#q
                print(self.commandList[5])
                break
            elif(command[0]==self.commandList[6]):#traceroute
                print(self.commandList[6])
                TraceRoute(self.lk,self.node_info)
                
        
if __name__=="__main__":

    node=Node(sys.argv[1])
    x=threading.Thread(target=node.run)
    x.start()

    link=node.lk
    link.recievingData()

