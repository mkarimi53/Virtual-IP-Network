import struct,socket


class IPPacket:
    def assignValues(self,headerLength,totalLength,id,fragFlag,fragOffset,src,dst,protocol,ttl,ICMPtype,irfh,packet):
      self.headerLength=headerLength 
      self.totalLength=totalLength 
      self.id=id# something line seq number unique for every packet in maximum datagram life time
      self.fragFlag=fragFlag #boolean value for packets that is fragmentated  or all other required flags
      self.fragOffset=fragOffset 
      self.src=socket.inet_aton(src)
      self.dst=socket.inet_aton(dst)
  #    self.checksum=checksum#shit in mage mikhad piade sazi O_o
      self.protocol=protocol# unsigned char differentiate between routing packets and other boolean value (0 or 200)
      self.TTL=ttl #useful for ICMP
      #self.ICMPtype=ICMPtype #only destincation unreachable???becuase of ttl timeout
      self.ICMPredirectFromHost=socket.inet_aton(irfh) #for trace route
      self.packet=packet #type string
      checkSum(totalLength) #ok what the is n???????/
    def pack(self):
      #little endian
      #H 2byte B 1byte I 4byte s for string
      raw=struct.pack('<HHI?H4s4sBH4s'+str(self.totalLength-self.headerLength)+'s',\
        self.headerLength,\
        self.totalLength,\
        self.id,\
        self.fragFlag,\
        self.fragOffest,\
        self.src,\
        self.dst,\
        self.protocol,\
        self.TTL,\
        self.ICMPredirectFromHost,\
        bytearray(self.packet,'utf-8')
      )
      return raw
      
    def unpack(self,bytearrayPacket):
      headerLengthTuple=struct.unpack('<HH',bytearrayPacket[:4])
      self.headerLength=headerLengthTuple[0]
      self.totalLength=headerLengthTuple[1]
      headerTuple=struct.unpack('<HHH?H4s4sBH4s'+str(self.totalLength-self.headerLength)+'s',bytearrayPacket)
      # self.headerLength=headerTuple[]
      # self.totalLength=headerTuple[]
      self.id=headerTuple[2]
      self.fragFlag=headerTuple[3]
      self.fragOffest=headerTuple[4]
      self.src=headerTuple[5]
      self.dst=headerTuple[6]
      self.protocol=headerTuple[7]
      self.TTL=headerTuple[8]
      self.ICMPredirectFromHost=headerTuple[9]
      self.packet=headerTuple[10].decode('utf-8')



    def checkSum(n):# whaat is n?? is it n? 
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
      self.checksum=answer             
      return answer


