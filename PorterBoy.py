import sys, socket
from datetime import datetime as dt
from colorama import Fore, Style, Back	


target = None
t1 = dt.now()

def scanner():
	global target

	if len(sys.argv) == 2:
		target = socket.gethostbyname(sys.argv[1])
	else:
		print("invalid amount of arguments.")
		sys.exit()

def porter():
	global start_port, final_port

	print(Fore.BLUE + '-' * 60)
	print('Scanning target '+target)
	print('Time started: '+str(dt.now()))
	print('-' * 60)
	Style.RESET_ALL

	start_port = int(input('Choose the start port: '))
	final_port = int(input('Choose the final port: '))

def try_except():
	global portLST
	portLST = []
	sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		for ports in range(start_port, final_port+1):
			sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			#socket.setdefaulttimeout(0.5)
			result = sckt.connect_ex((target, ports))
	
			if result == 0:
				print(Fore.GREEN + f'Port {ports} is open')
				Style.RESET_ALL
				portLST.append(ports)
				sckt.close()

			else:
				print(Fore.RED + f'Port {ports} is closed')
				Style.RESET_ALL

	except KeyboardInterrupt:
		print('\nEnding program.')
		sys.exit()

	except socket.gaierror:
		print('Invalid hostname')
		sys.exit()

	except socket.error:
		print("Couldn't connect to server, check your wifi.")
		sys.exit()


def main():
	scanner()
	porter()
	try_except()
	
	if 'y' in input('Would you like a summary?\n(y/n)> '):
		print(Fore.MAGENTA + f'{portLST}')
	else:
		sys.exit()

	t2 = dt.now()
	tt = t2 - t1
	print(Fore.LIGHTRED_EX + f'{tt}')

if __name__ == '__main__':
	main()
