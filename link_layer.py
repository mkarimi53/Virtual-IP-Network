import socket, threading, sys, time
from node_info import Link_info, Node_info
from IP import IPPacket
#from traceroute import TraceRoute


class LinkLayer:
    DataLoadLimit=1400
    #un baba 64KB chi mige ???
    def __init__(self,port,bufferSize):
        self.localPort=port
        self.localIP="127.0.0.1"
        self.bufferSize=bufferSize
        self.UDPSocket=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)       
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


class BroadCast:
    port=10100
    def sendBroadCast(self,message):
        dest = ('255.255.255.255',BroadCast.port)
        self.sendSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sendSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sendSock.sendto(message.encode('utf-8'), dest)

    def receiveBroadCast(self):
        self.recieveSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recieveSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recieveSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.recieveSock.bind(("255.255.255.255",BroadCast.port))
             
        while(True):
            try:
                print("listening to broadcast")
                message, address = self.recieveSock.recvfrom(10104)
                print(message.decode())
            except socket.error as r:
                print(r)

class RoutingTable:
    def __init__(self, start):
        self.num_nodes = 0
        self.nodes_index = {}
        self.table = []
        self.distances = {}
        self.nodes = []
        self.readFile()
        self.start = self.nodes_index[start]
        self.set_distances()
        self.visited = {node: None for node in nodes}    #keeps distances from start to each node that has been visited
        self.previous = {node: None for node in nodes}   
        self.dijkstra()
        # self.show()

    def readFile(self):
        net_lines = []
        with open('nets/ABC.net') as net_file:
            for line in net_file:
                net_lines.append(line[:-1])

        self.num_nodes = 0
        for line in net_lines:
            words = line.split(' ')
            if words[0] == 'node':
                self.nodes_index[words[1]] = self.num_nodes
                self.num_nodes += 1
            else:
                break
        
        for row in range(self.num_nodes):
            self.table.append([])
            for col in range(self.num_nodes):
                if row == col:
                    self.table[row].append(0)
                else:
                    self.table[row].append(-1)
        
        for line in net_lines:
            words = line.split(' ')
            if words[0] == 'node':
                continue

            self.table[self.nodes_index[words[0]]][self.nodes_index[words[2]]] = 1
            self.table[self.nodes_index[words[2]]][self.nodes_index[words[0]]] = 1
        
    def set_distances(self):
        for i in range(self.num_nodes):
            tempdict = {}
            for j in range(self.num_nodes):
                if i!=j and self.table[i][j]!=-1:
                    tempdict[j] = self.table[i][j]
            self.distances[i] = tempdict
            self.nodes.append(i)

    def show(self):
        for row in range(self.num_nodes):
            for col in range(self.num_nodes):
                print(self.table[row][col], end=', ')
            print()

    def dijkstra(self):
        nodes = self.nodes
        distances = self.distances

        unvisited = {node: None for node in nodes}  #keeps distances from start to each node that is yet unvisited

        current = self.start
        currentDist = 0
        unvisited[current] = currentDist

        while True:
            for next, distance in distances[current].items():

                if next not in unvisited: continue
                
                newDist = currentDist + distance

                if not unvisited[next] or unvisited[next] > newDist:
                    unvisited[next] = newDist
                    self.previous[next] = current

            self.visited[current] = currentDist
            del unvisited[current]
            
            done = 1
            for x in unvisited:
                if unvisited[x]:
                    done = 0
                    break
            if not unvisited or done:
                break

            elements = [node for node in unvisited.items() if node[1]]

            current, currentDist = sorted(elements, key = lambda x: x[1])[0]

        return

    def shortest_path(self, end):
        path = []
        dest = end
        src = self.start
        path.append(dest)

        while dest != src:
            path.append(previous[dest])
            dest = previous[dest]

        path.reverse()

    def buildForwardingTable(self):
        return {}   #A dictionary with destination (ip, port) key and the next hub (ip, port) as value

class Node:
    def  __init__(self,filePath):     
        self.commandList=["interfaces","routes","down","up","send","q","traceroute"]
        self.node_info=Node_info(filePath)
        self.lk=LinkLayer(self.node_info.lport,100)
        self.broadCast=BroadCast()
        self.routingTable = RoutingTable()
        self.forwardingTable = self.routingTable.buildForwardingTable()

    # def SetTraceRouteAgent(self,tr):
    #     self.traceRouteAgent=tr #for node that call traceroute

    def sendIPMessageToDst(self,dstIP,message):
        #ippacket=IPPacket()
        #find interface and next node from routing table 
        #ippacket.assignValues(dataLength,id,fragFlag,fragOffset,src,dst,protocol,ttl,ICMPtype,irfh,packet)
        self.lk.sendData(dstIP,message.encode('utf-8'))           

    def runCommandLine(self):
        while(True):
            commandraw=input(">")
            command=commandraw.split(" ")

            if(command[0]==self.commandList[0]):#interfaces
                for x in self.node_info.remotes:
                    print(x.remote_host,x.remote_port,x.local_virt_ip,x.remote_virt_ip)

            elif(command[0]==self.commandList[1]):#routes
                self.br.sendBroadCast("hhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                print(self.commandList[1])

            elif(command[0]==self.commandList[2]):#down
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

            else:
                print('command is invalid')

    def run(self):
        commandLine=threading.Thread(target=self.runCommandLine)
        commandLine.start()

        receiveNetworkChange=threading.Thread(target=self.broadCast.receiveBroadCast)
        receiveNetworkChange.start()

        while(self.lk.recieving):
            data=self.lk.recievingData()
            print(data.decode())
            # packet=IPPacket()
            # packet.unpackIPv4(data)
            # if(packet.protocol==0):
            #    print("resend after routing or print it")
            # elif(packet.protocol==200):
            #    traceRouteOperation(node, tr, packet)


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


if __name__=="__main__":
    node=Node(sys.argv[1])
    node.run()
    # tr=TraceRoute()
    # node.SetTraceRouteAgent(tr)