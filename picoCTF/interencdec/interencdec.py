import base64

enc_flag = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg=="
decoded_bytes = base64.b64decode(enc_flag)
decoded_decoded_bytes = base64.b64decode(decoded_bytes.decode().strip()[2:-1]).decode().strip()

for i in range(26):
  flag = ''
  for c in decoded_decoded_bytes:
    if c.islower():
      flag += chr((ord(c) - ord('a') - i) % 26 + ord('a'))
    elif c.isupper():
      flag += chr((ord(c) - ord('A') - i) % 26 + ord('A'))
    else:
      flag += c
  print(flag)
