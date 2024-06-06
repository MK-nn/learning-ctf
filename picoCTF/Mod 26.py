cipher = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
flag = ""

for c in cipher:
    if c.islower():
        flag += chr((ord(c) - ord('a') - 13) % 26 + ord('a'))
    elif c.isupper():
        flag += chr((ord(c) - ord('A') - 13) % 26 + ord('A'))
    else:
        flag += c

print(flag)