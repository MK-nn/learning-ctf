import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "abcdefghijklmnopqrstuvwxyzPQRSTUVWXYZ0123456789"
for key in "ef":
  assert all([k in ALPHABET for k in key])
  assert len(key) == 1

  b16 = b16_encode(flag)
  enc = ""
  enc_array = []
  for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])
  for i in range(len(enc)):
      if i % 2 == 0:
        enc_array.append(enc[i])
  print(key, set(enc_array))
	
