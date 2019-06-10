import socket, threading,sys,selectors
import node_info
class linklayer:
    __init__(self,port,bufferSize):
        self.localport=port
        self.interfaces=interfaces
        self.localip="127.0.0.1"
        self.bufferSize=bufferSize
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.DPServerSocket.bind((self.localIP, self.localPort))
        self.recieving=True
    
    sendData(self,srcIP,dstIP,port):
        UDPClientSocket.sendto(bytesToSend, (dstIP,port))
    
    recievingData(self):
        while(recieving):
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
 
class linklayerThreaded(threading.Thread):
    __init__(self,port,bufferSize):
        threading.Thread.__init__(self)
        self.localport=port
        self.interfaces=interfaces
        self.localip="127.0.0.1"
        self.bufferSize=bufferSize
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.DPServerSocket.bind((self.localIP, self.localPort))
        self.recieving=True

    sendData(self,srcIP,dstIP,port):
        UDPClientSocket.sendto(bytesToSend, (dstIP,port))

    recievingData(self):
        while(recieving):
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            print(msgFromServer)


class Node:
    __init__(self,filePath):
        self.commandList=["interfaces","routes","down","up","send","q","traceroute"]
        self.node_info=Node_info(filePath)
        self.lk=linklayer(self.node_info.lport,100)


    run(self):
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
                node_info.send()
                self.node_info.remotes[interfaceNum].remote_port
                print(self.commandList[4])
            elif(command[0]==self.commandList[5]):#q
                print(self.commandList[5])
            elif(command[0]==self.commandList[6]):#traceroute
                print(self.commandList[6])
        
if __name__=="__main__":
    
    node=Node()
    nodeThread=linklayerThreaded(node.node_info.lport,100)
    nodeThread.recievingData()
    node.run()
