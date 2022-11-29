#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) == "e":
        continue
    if chr(i) == "q":
        continue
    print("{}".format(chr(i)), end="")
