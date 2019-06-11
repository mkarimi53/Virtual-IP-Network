class IPPacket:
    def __init___(self,headerLength,version,totalLength,id,fragFlag,fragOffset,src,dst,protocol,ttl,ICMPtype,ICMPredirectFromHost,packet):
      self.headerLength=headerLength
      self.version=version
      self.totalLength=totalLength
      self.id=id# something line seq number unique for every packet in maximum datagram life time
      self.fragFlag=fragFlag #boolean value for packets that is fragmentated 
      self.fragOffset=fragOffset # 
      self.src=src
      self.dst=dst
  #    self.checksum=checksum#shit in mage mikhad piade sazi O_o
      self.protocol=protocol# differentiate between routing packets and other boolean value (0 or 200)
      self.TTL=ttl #useful for ICMP
      #DSCP required? (type of service)

      #ICMP headers
      self.ICMPtype=ICMPtype #only destincation unreachable???becuase of ttl timeout
      self.ICMPredirectFromHost=irfh #for trace route
      self.packet=packet
      checkSum(totalLength) #ok what the is going to be this number???????/
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


