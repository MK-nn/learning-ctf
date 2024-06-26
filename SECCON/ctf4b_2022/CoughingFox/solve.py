import gmpy2

cipher = [12147, 20481, 7073, 10408, 26615, 19066, 19363, 10852, 11705, 17445, 3028, 10640, 10623, 13243, 5789, 17436, 12348, 10818, 15891, 2818, 13690, 11671, 6410, 16649, 15905, 22240, 7096, 9801, 6090, 9624, 16660, 18531, 22533, 24381, 14909, 17705, 16389, 21346, 19626, 29977, 23452, 14895, 17452, 17733, 22235, 24687, 15649, 21941, 11472]
flag = b"ctf4b{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"

flags = []
for c in cipher:
  for i in range(len(flag)):
    a,b = gmpy2.iroot(c - i, 2)
    if b == True:
      f = a - i
      flags.append({'index': i, 'value': f})
      break

flags.sort(key=lambda x: x['index'])

flag = ""
for f in flags:
  flag += chr(f['value'])

print(flag)
