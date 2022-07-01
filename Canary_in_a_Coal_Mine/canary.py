#!/bin/python
from pwn import*
target = process ("./canary")

print(target.recvline()) # What is the capital of Canada?
print(target.recvline()) # What is the length of your answer?

target.sendline(b"6")

print(target.recvline()) # Give me your answer

target.sendline(b"ottawa")

print(target.recvline()) # Want to change your answer?
print(target.recvline()) # Here is a second try

target.sendline(b"ottawa")

print(target.recvline()) # Still wrong! Nerd
