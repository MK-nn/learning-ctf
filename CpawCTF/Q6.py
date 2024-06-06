cipher = 'fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}'
flag = ''

for c in cipher:
    if c.islower():
        flag += chr((ord(c) - ord('a') - 3) % 26 + ord('a'))
    elif c.isupper():
        flag += chr((ord(c) - ord('A') - 3) % 26 + ord('A'))
    else:
        flag += c

print(flag)