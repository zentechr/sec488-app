#!/usr/bin/python3

import random

access_key = "AKIA"
secret_key = ""

counter = 0
while counter < 12:
    ascii_val = random.randrange(48,90)
    if ((ascii_val < 58) or (ascii_val > 64)):
        access_key += chr(ascii_val)
        counter += 1

counter = 0
while counter < 40:
    ascii_val = random.randrange(47,122)
    if ((ascii_val < 58) or (ascii_val > 64 and ascii_val < 91) or (ascii_val > 96)):
        secret_key += chr(ascii_val)
        counter += 1

f = open("./totally-not-keys.txt", "w")
f.write("[default]\n")
f.write("aws_access_key_id = " + access_key + "\n")
f.write("aws_secret_access_key = " + secret_key + "\n")
