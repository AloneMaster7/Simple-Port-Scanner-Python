import socket

ip = "127.0.0.1"
ports = [21,22,23,443,80]
for port in range(1,1023):
    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
    r = s.connect_ex((ip,port))
    rslt = "not open"
    if r is 0:
        rslt = "open"
    print(port,":",rslt)
    s.close()
