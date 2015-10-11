import random
 
class IPGen():
        def __init__(self):
                pass
        def ip2hex (self,ip):
                return hex(struct.unpack("!I", socket.inet_aton(ip))[0])
     
        def ip2long (self,ip):
 
                quads = ip.split('.')
                 
                if len(quads) == 1:
                        # only a network quad
                        quads = quads + [0, 0, 0]
                elif len(quads) < 4:
                        # partial form, last supplied quad is host address, rest is network
                        host = quads[-1:]
                        quads = quads[:-1] + [0, ] * (4 - len(quads)) + host
 
                lngip = 0
                for q in quads:
                        lngip = (lngip << 8) | int(q)
                return lngip 
 
        def long2ip (self,l):
                MIN_IP = 0x0
                MAX_IP = 0xffffffff
                #return socket.inet_ntoa(struct.pack("!L", lint))
                if MAX_IP < l or l < MIN_IP:
                        print 'test1'
                        raise TypeError("expected int between %d and %d inclusive" % (MIN_IP, MAX_IP))
                return '%d.%d.%d.%d' % (l >> 24 & 255, l >> 16 & 255, l >> 8 & 255, l & 255)
 
        '''
        61.232.0.0-61.237.255.255
        106.80.0.0-106.95.255.255
        121.76.0.0-121.77.255.255
        123.232.0.0-123.235.255.255
        139.196.0.0-139.215.255.255
        171.8.0.0-171.15.255.255
        182.80.0.0-182.92.255.255
        210.25.0.0-210.47.255.255
        222.16.0.0-222.95.255.255
        '''
        def ip(self):
                ip_long = [        
                        [self.ip2long('61.232.0.0'), self.ip2long('61.237.255.255')],
                        [self.ip2long('106.80.0.0'), self.ip2long('106.95.255.255')],
                        [self.ip2long('121.76.0.0'), self.ip2long('121.77.255.255')],
                        [self.ip2long('123.232.0.0'), self.ip2long('123.235.255.255')],
                        [self.ip2long('139.196.0.0'), self.ip2long('139.215.255.255')],
                        [self.ip2long('171.8.0.0'), self.ip2long('171.15.255.255')]
                        ]
 
                rand_key = random.randint(0,4)
                #print self.long2ip(2130706433)
                #print self.ip2long('61.232.0.0')
                #print self.ip2long('61.237.255.255')
                return self.long2ip(random.randint(ip_long[rand_key][0], ip_long[rand_key][1]))
                #return self.long2ip(-569376768)
