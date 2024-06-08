enc_flag = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"
key = "f"
b16 = ''

for c in enc_flag:
  i = ord(c) - ord('a') - (ord(key) - ord('a'))
  if i >= 0:
    
    b16 += chr(i + ord('a'))
  else:
    b16 += chr(i + ord('a') + 16)

flag = ''
for i in range(0, len(b16), 2):
  flag += chr(int("{0:04b}".format(ord(b16[i]) - ord('a')) + "{0:04b}".format(ord(b16[i+1]) - ord('a')), 2))

print(flag)
