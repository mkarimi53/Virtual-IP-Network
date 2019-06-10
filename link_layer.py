import socket, threading,sys,selectors
from node_info import Link_info,Node_info
class linklayer:
    def __init__(self,port,bufferSize):
        self.localPort=port
        self.localIP="127.0.0.1"
        self.bufferSize=bufferSize
        self.UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        
        self.UDPSocket.bind((self.localIP, self.localPort))
        self.UDPSocket.setblocking(False)
        self.recieving=True
    
    def sendData(self,port,data):
        self.UDPSocket.sendto(data.encode(), (self.localIP,port))
    
    def recievingData(self):
        print("recieving")
        while(self.recieving):
            msgFromServer = self.UDPSocket.recvfrom(self.bufferSize)
            print(msgFromServer.decode())

 
class linklayerThreaded(threading.Thread):
    def __init__(self,UDPSocket,bufferSize):
        threading.Thread.__init__(self)
        self.localIP="127.0.0.1"
        self.bufferSize=bufferSize
        self.UDPSocket = UDPSocket
        self.recieving=True

    def sendData(self,port,massage):
        self.UDPSocket.sendto(message.encode(), (self.localIP,port))

    def run(self):
        print("recieving")
        while(self.recieving):
            try:
                msgFromServer = self.UDPSocket.recvfrom(self.bufferSize)
            except socket.error as r:
                print("i got error")
                print(r)
            print(msgFromServer.decode())


class Node:
    def  __init__(self,filePath):
        self.commandList=["interfaces","routes","down","up","send","q","traceroute"]
        self.node_info=Node_info(filePath)
        self.lk=linklayer(self.node_info.lport,100)


    def run(self):
        print("hey")
        while(True):
            commandraw=input(">")
            command=commandraw.split(" ")
            if(command[0]==self.commandList[0]):#interfaces
                print(self.commandList[0])
            elif(command[0]==self.commandList[1]):#routes
                print(self.commandList[1])
            elif(command[0]==self.commandList[2]):#down
                print(self.commandList[2])
            elif(command[0]==self.commandList[3]):#up
                print(self.commandList[3])
            elif(command[0]==self.commandList[4]):#send
                interfaceNum=int(command[1])
                node_info.send(command[2],self.node_info.remotes[interfaceNum].remote_port)
                
                print(self.commandList[4])
            elif(command[0]==self.commandList[5]):#q
                print(self.commandList[5])
            elif(command[0]==self.commandList[6]):#traceroute
                print(self.commandList[6])
        
if __name__=="__main__":
    
    node=Node(sys.argv[1])
    nodeThread=linklayerThreaded(node.lk.UDPSocket,10)
    nodeThread.run()
    print("what the hell")
    node.run()
