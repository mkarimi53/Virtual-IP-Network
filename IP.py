import struct,socket


class IPPacket:
    def assignValues(self,dataLength,id,fragFlag,fragOffset,src,dst,protocol,ttl,ICMPtype,irfh,packet):
      self.headerLength=31 #update due to changes
      self.dataLength=dataLength
      self.id=id# something line seq number unique for every packet in maximum datagram life time
      self.fragFlag=fragFlag #boolean value for packets that is fragmentated  or all other required flags
      self.fragOffset=fragOffset 
      self.src=src
      self.dst=dst
      self.protocol=protocol# unsigned char differentiate between routing packets and other boolean value (0 or 200)
      self.TTL=ttl #useful for ICMP
      self.ICMPtype=ICMPtype #1->routing packet 2->timeout packet 3->destination reached 4->destination not reached
      self.expectedHost=irfh #in dst interface router ghabli ke az tarighesh be in node residim
      self.packet=packet #type string
      self.checkSum=self.checkSumCalculator(self.dataLength) #ok what the is nBBBBBBB/
      
    def packIPv4(self):
      #little endian
      #H 2byte B 1byte I 4byte s for string een alan 31 byte headersh kolan
      if(self.dataLength>0):
        raw=struct.pack('<HHIBH4s4sBHB4sI'+str(self.dataLength)+'s',\
          self.headerLength,\
          self.dataLength,\
          self.id,\
          self.fragFlag,\
          self.fragOffset,\
          socket.inet_aton(self.src),\
          socket.inet_aton(self.dst),\
          self.protocol,\
          self.TTL,\
          self.ICMPtype,\
          socket.inet_aton(self.expectedHost),\
          self.checkSum,\
          bytearray(self.packet,'utf-8'))
        return raw
      else:
        raw=struct.pack('<HHIBH4s4sBHB4sI',\
          self.headerLength,\
          self.dataLength,\
          self.id,\
          self.fragFlag,\
          self.fragOffset,\
          socket.inet_aton(self.src),\
          socket.inet_aton(self.dst),\
          self.protocol,\
          self.TTL,\
          self.ICMPtype,\
          socket.inet_aton(self.expectedHost),\
          self.checkSum)
        return raw

    def unpackIPv4(self,bytearrayPacket):
      headerLengthTuple=struct.unpack('<HH',bytearrayPacket[:4])
      self.headerLength=headerLengthTuple[0]
      self.dataLength=headerLengthTuple[1]
      if(self.dataLength>0):
        headerTuple=struct.unpack('<HHIBH4s4sBHB4sI'+str(self.dataLength)+'s',bytearrayPacket)
        self.id=headerTuple[2]
        self.fragFlag=headerTuple[3]
        self.fragOffset=headerTuple[4]
        self.src=socket.inet_ntoa(headerTuple[5])
        self.dst=socket.inet_ntoa(headerTuple[6])
        self.protocol=headerTuple[7]
        self.TTL=headerTuple[8]
        self.ICMPtype=headerTuple[9]
        self.expectedHost=socket.inet_ntoa(headerTuple[10])
        self.checkSum=headerTuple[11]
        self.packet=headerTuple[12].decode('utf-8')
      else:
        headerTuple=struct.unpack('<HHIBH4s4sBHB4sI',bytearrayPacket)
        self.id=headerTuple[2]
        self.fragFlag=headerTuple[3]
        self.fragOffset=headerTuple[4]
        self.src=socket.inet_ntoa(headerTuple[5])
        self.dst=socket.inet_ntoa(headerTuple[6])
        self.protocol=headerTuple[7]
        self.TTL=headerTuple[8]
        self.ICMPtype=headerTuple[9]
        self.expectedHost=socket.inet_ntoa(headerTuple[10])
        self.checkSum=headerTuple[11]

    def checkSumCalculator(self,n):# whaat is nBB is it nB 
      #check sum bara header e ya packet BBBB
      sum=0
      if(self.dataLength==0):
        return 0
      odd_byte=0
      counterIndex=0
      for c in self.packet:
        sum+=ord(c)
        n-=2
        counterIndex+=1
        if(n <=1):
          break
      counterIndex+=1
      if(n==1):
        sum+=ord(packet[counterIndex])
      sum = (sum >> 16) + (sum & 0xffff)
      sum += (sum >> 16)
      answer = ~sum
      return answer


