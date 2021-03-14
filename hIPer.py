from datetime import datetime as dt
import socket
from colorama import Fore, init

ogNet = input('IP starter\n>: ')
begin = int(input('Enter First #\n>: '))
end = int(input('Enter Last #\n>: '))

Net = ogNet.split('.')

Net2 = Net[0] + '.' + Net[1] + '.' + Net[2] + '.'
end += 1

t1 = dt.now()

def scan(addr):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(0.1)
	result = s.connect_ex((addr, 22)) #gotta fix this dude, maybe throw in a s.bind(('HOST', PORT)) and listen or sometiny
	if result == 0:
		init(autoreset=True)
		print(Fore.GREEN + "{} is live".format(addr))
	else:
		print("{} is dead".format(addr))

def run1():
	for ip in range(begin, end):
		addr = Net2 + str(ip)
		
		scan(addr)

run1()
t2 = dt.now()
tt = t2 - t1
print('-' * 50)
print("Scanning Completed In: {}".format(tt))
print('-' * 50)
