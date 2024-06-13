flag = "gvswwmrkxlivyfmgsrhnrisegl"

for i in range(1, 26):
    print("picoCTF{" + "".join([chr((ord(c) - ord('a') - i) % 26 + ord('a')) for c in flag]) + "}")
