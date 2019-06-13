import socket, threading,sys,time
from node_info import Link_info,Node_info
from IP import IPPacket
#from traceroute import TraceRoute


class LinkLayer:
    DataLoadLimit=1400
    #un baba 64KB chi mige ???
    def __init__(self,port,bufferSize):
        self.localPort=port
        self.localIP="127.0.0.1"
        self.bufferSize=bufferSize
        self.UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)       
        self.UDPSocket.bind((self.localIP, self.localPort))
        self.recieving=True
    
    
    def sendData(self,port,data):
        self.UDPSocket.sendto(data, (self.localIP,port))
    
    def recievingData(self):
        try:
            msgFromServer = self.UDPSocket.recvfrom(self.bufferSize)
            return msgFromServer
        except socket.error as r:
            print("i got error",r)

class Node:
    def  __init__(self,filePath):     
        self.commandList=["interfaces","routes","down","up","send","q","traceroute"]
        self.node_info=Node_info(filePath)
        self.lk=LinkLayer(self.node_info.lport,100)
    # def SetTraceRouteAgent(self,tr):
    #     self.traceRouteAgent=tr #for node that call traceroute
    def SetBroadCast(self,br):
        self.br=br

    def sendIPMessageToDst(self,dstIP,message):
        #
        #ippacket=IPPacket()
         #find interface and next node from routing table 
        #ippacket.assignValues(dataLength,id,fragFlag,fragOffset,src,dst,protocol,ttl,ICMPtype,irfh,packet)
        self.lk.sendData(dstIP,message.encode('utf-8'))           

    def run(self):
        while(True):
            commandraw=input(">")
            command=commandraw.split(" ")
            if(command[0]==self.commandList[0]):#interfaces
                for x in self.node_info.remotes:
                    print(x.remote_host,x.remote_port,x.local_virt_ip,x.remote_virt_ip)
            elif(command[0]==self.commandList[1]):#routes
                self.br.sendBroadCast("hhhhhhhhhhhhhhhhhhhhhhhhhhhh")
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
            #   self.traceRouteAgent.run()    
def traceRouteOperation(node,tr,packet):
    #def assignValues(self,dataLength,id,fragFlag,fragOffset,src,dst,protocol,ttl,ICMPtype,irfh,packet):

    if(packet.ICMPtype==1):#routing packet
        print("implement later")
    elif(packet.ICMPtype==2):#ttl timeout 
        print("implement later")

    elif(packet.ICMPtype==3):#destination reached
        print("implement later")
    elif(packet.ICMPtype==4):#destination not reached
        print("implement later")

class BroadCast:
    port=10100
    def sendBroadCast(self,message):
        dest = ('127.0.0.1',BroadCast.port)
        self.sendSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sendSock.sendto(message.encode('utf-8'), dest)
    def receiveBroadCast(self):
        while(True):
            try:
                print("listening to broadcast")
                self.recieveSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.recieveSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.recieveSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                self.recieveSock.bind(("127.0.0.1",BroadCast.port))
                message, address = self.recieveSock.recvfrom(10104)
                print(message.decode())
                self.recieveSock.close()
                self.sendBroadCast(message.decode())
                time.sleep(2)
            except socket.error as r:
                print(r)
        
if __name__=="__main__":

    node=Node(sys.argv[1])
    # tr=TraceRoute()
    br=BroadCast()
    # node.SetTraceRouteAgent(tr)
    node.SetBroadCast(br)
    x=threading.Thread(target=node.run)
    x.start()
    y=threading.Thread(target=br.receiveBroadCast)
    y.start()
    link=node.lk
    while(link.recieving):
        data=link.recievingData()
        print(data.decode())
  #      packet=IPPacket()
 #       packet.unpackIPv4(data)
#        if(packet.protocol==0):
#            print("resend after routing or print it")
#        elif(packet.protocol==200):
#            traceRouteOperation(node,tr,packet)



