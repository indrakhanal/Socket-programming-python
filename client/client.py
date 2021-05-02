import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1026))
all_info = ''
while True:
    msg = s.recv(10)
    if len(msg) == 0:
        break
    all_info += msg.decode("utf-8")
print(all_info)