# coding: utf8
import json
import struct
import socket
import asyncore
from cStringIO import StringIO

class RPCHandler(asyncore.dispatcher_with_send):

    def __init__(self, sock, addr):
        asyncore.dispatcher_with_send.__init__(self, sock=sock)
