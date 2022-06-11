#!/usr/bin/python3

#Usage: python3 <First 3 octets i.e 10.0.0> <First forth octet> <Last forth octet> 
import os 
import sys

a=sys.argv[1]
b=int(sys.argv[2])
c=int(sys.argv[3])
c=c+1
for x in range(b, c):
        
        d =  (a + "." + str(x))

        response = os.system("ping %s -c 1 > /dev/null" %d)
        
        if response == 0:
                print("%s" %d)
