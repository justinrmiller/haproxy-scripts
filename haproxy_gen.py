#!/usr/bin/env python

import sys

# a hacky little script to take a base config string and
# append a space separated input of IP addresses to it

base_conf = """
global 
      maxconn 4096 
      pidfile /var/run/haproxy.pid 
      daemon 

defaults 
      mode http 
      retries 3 
      option redispatch 
      maxconn 2000 
      contimeout 5000 
      clitimeout 50000 
      srvtimeout 50000 

listen CLUSTER 0.0.0.0:80
      mode http 
      balance roundrobin 
      option httpclose 
      option forwardfor 
      stats enable 
      stats auth myuser:mypass
      stats realm Strictly\ Private
      stats uri /stats   
"""

print base_conf

for ip_address in sys.argv[1:]:
	print "      server " + ip_address + " " + ip_address + ":8080 check" 
