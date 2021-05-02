import socket
import pickle

a = 10
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind((socket.gethostname(), 2133))
s1.listen(5)
host = socket.gethostname()
print('hostname:', host)
while True:
    clt, adr = s1.accept()
    print(f'connection to {adr} established')
    m = {1: "Client", 2: "server"}
    mymsg = pickle.dumps(m)
    mymsg = bytes(f'{len(mymsg):<{a}}', "utf-8") + mymsg
    clt.send(mymsg)
    clt.close()
