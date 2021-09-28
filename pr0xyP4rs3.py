#!/usr/bin/python
import requests
import sys

url = sys.argv[2]
proxies = {"http": "http://127.0.0.1:7777", "https": "http://127.0.0.1:7777"}

def banner():
	
	print (" .-----------------------------.           ")
	print (" |  Hi Hackers                 |           ")
	print (" |  Tool   : pr0xyP4rs3        |")
	print (" |  Author : @karthi_the_hacker|           ")
	print (" |           Jai Hind          |           ")
	print (" '-----------------------------'           ")
	print ("                 ^      (\_/)    ")
	print ("                 '----- (O.o)    ")
	print ("                        (> <)    ")
	print (" ")


def helpl():
	banner()
	print ("For single domain   : python pr0xyP4rs3.py -p http://yourserver.com/ ")
	print ("For multiple domain : cat live-domain.txt | xargs -n1 -p50 python pr0xyP4rs3.py --parse  " )

def all():
	r  = requests.get(url , proxies=proxies , allow_redirects=False ,verify=False )
	r1 = requests.get(url , proxies=proxies ,verify=False )
	R  = requests.post(url , proxies=proxies , allow_redirects=False ,verify=False )
	R1 = requests.post(url , proxies=proxies ,verify=False )
	Rp  = requests.put(url , proxies=proxies , allow_redirects=False ,verify=False )
	Rp1 = requests.put(url , proxies=proxies ,verify=False )

if (len(sys.argv)<=1):
	banner()
	print("You must provide a target. Use -h or --help for help.")
	print(" ")
	sys.exit()

if (str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help"):
	helpl()
	sys.exit()

if (str(sys.argv[1]) == "-p" or str(sys.argv[1]) == "--parse"):
	all()
url = sys.argv[2]
