import  socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1026))
s.listen(5)
while True:
    clt, adr = s.accept()
    print(f'connection to {adr} established')
    clt.send(bytes("socket programming in python", "utf-8"))
    clt.close()


