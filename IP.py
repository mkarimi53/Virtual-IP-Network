import struct,socket


class IPPacket:
    def assignValues(self,dataLength,id,fragFlag,fragOffset,src,dst,protocol,ttl,ICMPtype,irfh,packet):
      self.headerLength=31 #update due to changes
      self.dataLength=dataLength
      self.id=id# something line seq number unique for every packet in maximum datagram life time
      self.fragFlag=fragFlag #boolean value for packets that is fragmentated  or all other required flags
      self.fragOffset=fragOffset 
      self.src=socket.inet_aton(src)
      self.dst=socket.inet_aton(dst)
      self.protocol=protocol# unsigned char differentiate between routing packets and other boolean value (0 or 200)
      self.TTL=ttl #useful for ICMP
      self.ICMPtype=ICMPtype #1->routing packet 2->timeout packet 3->destination reached 4->destination not reached
      self.ICMPdirectFromHost=socket.inet_aton(irfh) #in dst interface router ghabli ke az tarighesh be in node residim
      self.packet=packet #type string
      self.checkSum=checkSumCalculator(dataLength) #ok what the is n???????/
    def packIPv4(self):
      #little endian
      #H 2byte B 1byte I 4byte s for string een alan 26 byte headersh kolan
      raw=struct.pack('<HHI?H4s4sBHBI4s'+str(self.dataLength)+'s',\
        self.headerLength,\
        self.dataLength,\
        self.id,\
        self.fragFlag,\
        self.fragOffest,\
        self.src,\
        self.dst,\
        self.protocol,\
        self.TTL,\
        self.ICMPtype,\
        self.ICMPdirectFromHost,\
        self.checkSum
        bytearray(self.packet,'utf-8'))
      return raw
      
    def unpackIPv4(self,bytearrayPacket):
      headerLengthTuple=struct.unpack('<HH',bytearrayPacket[:4])
      self.headerLength=headerLengthTuple[0]
      self.dataLength=headerLengthTuple[1]
      headerTuple=struct.unpack('<HHI?H4s4sBHBI4s'+str(self.dataLength)+'s',bytearrayPacket)
      self.id=headerTuple[2]
      self.fragFlag=headerTuple[3]
      self.fragOffest=headerTuple[4]
      self.src=socket.inet_ntoa(headerTuple[5])
      self.dst=socket.inet_ntoa(headerTuple[6])
      self.protocol=headerTuple[7]
      self.TTL=headerTuple[8]
      self.ICMPtype=headerTuple[9]
      self.ICMPdirectFromHost=socket.inet_ntoa(headerTuple[10])
      self.checkSum=headerTuple[11]
      self.packet=headerTuple[12].decode('utf-8')

    def checkSumCalculator(n):# whaat is n?? is it n? 
      #check sum bara header e ya packet ????
      sum=0
      odd_byte=0
      counterIndex=0
      for c in s:
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


