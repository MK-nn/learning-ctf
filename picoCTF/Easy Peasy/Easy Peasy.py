from pwn import *

host = 'mercury.picoctf.net'
port = 58913
KEY_LEN = 50000
FLAG_LEN = 32

io = remote(host, port)
for i in range(2):
    io.recvline()
encrypted_flag = io.recvuntil(b'\n\n').decode().strip()

io.recvuntil("What data would you like to encrypt?")
io.sendline(b'a'*(KEY_LEN-FLAG_LEN))
io.recvuntil("What data would you like to encrypt?")
io.sendline(b'a'*FLAG_LEN)
io.recvuntil("Here ya go!\n")
xor_a_and_key = io.recvuntil(b'\n\n').decode().strip()

print('encrypted_flag:', encrypted_flag)
print('xor_a_and_key:', xor_a_and_key)

flag = ''
for i in range(1, FLAG_LEN+1):
    flag += chr(int(encrypted_flag[i*2-2:i*2], 16) ^ int(xor_a_and_key[i*2-2:i*2], 16) ^ ord('a'))

print('flag:', flag)
