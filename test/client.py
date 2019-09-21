# coding: utf8

import json
import time
import socket
import struct

def receive(sock, n):
    rs = []  # 读取的结果
    while n > 0:
        r = sock.recv(n)
        if not r:  # EOF
            return rs
        rs.append(r)
        n -= len(r)
    return ''.join(rs)

def rpc(sock,in_,params):
    request = json.dumps({"in":in_ , "params":params})
    length_prefix = struct.pack("I",len(request))
    sock.send(length_prefix)
    sock.sendall(request)
    length_prefix = receive(sock,4)
    length, = struct.unpack("I",length_prefix)
    body = receive(sock,length)
    response = json.loads(body)
    return response["out"],response["result"]

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost",8081))
    for i in range(10):
        out,result = rpc(s, "ping", "ireader %d" % i)
        print(out, result)
        time.sleep(1)
    s.close()
