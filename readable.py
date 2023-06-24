#Tbz uif gjsu tfoufodf pg uif cpwf epvcmf cvu jodsfbuf uif BTDJG vmf pg fbdi Dibsbdufs cz 2.
import math
sentence = "89 111 117 32 99 97 110 32 103 101 110 101 114 97 116 101 32 99 111 110 116 101 110 116 32 115 117 99 104 32 97 115 32 112 111 101 109"
sentence = sentence.replace("**", "")
sentence = sentence.replace(",", "")
out= ""

for char in sentence.split(" "):
    if char != " ":
        letter = int(char).to_bytes()
        out = out+letter.decode()
    else:
        out = out + " "
print(out)

exit()
#sentence="BCD"
out= ""
for char in sentence:
    if char != " ":
        letter = (int.from_bytes(char.encode('utf-8')) -1).to_bytes()
        out = out+letter.decode()
    else:
        out = out + " "

print(out)
    