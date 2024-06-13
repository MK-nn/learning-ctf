enc_flag = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

flag = ''
for c in enc_flag:
    if c.islower():
        flag += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
    elif c.isupper():
        flag += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
    else:
        flag += c

print(flag)
      