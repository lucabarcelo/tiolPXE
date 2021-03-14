import threading
from queue import Queue
from datetime import datetime as dt
import socket, sys
from colorama import Fore, Style

print_lock = threading.Lock()

target = socket.gethostbyname(sys.argv[1])

print(Fore.BLUE + '-' * 60)
print('Scanning target '+target)
print('Time started: '+str(dt.now()))
print('-' * 60)
Style.RESET_ALL

start_port = int(input('Choose the start port: '))
final_port = int(input('Choose the final port: '))

def PorterMan(port):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sckt.connect((target, port))
        with print_lock:
            print(f'Port {port}')
        result.close()

    except KeyboardInterrupt:
        print('Cntrl + C pressed')

def threader():
    while True:
        worker = q.get()

        PorterMan(worker)

        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)

    t.daemon = True

    t.start()



for worker in range(start_port, final_port+1):
    q.put(worker)

q.join()

end = dt.now()

elapsed = start - end

print(f'Elapsed time {elapsed}')
