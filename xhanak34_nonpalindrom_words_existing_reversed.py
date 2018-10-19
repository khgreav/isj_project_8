#!/usr/bin/env python3

import fileinput

words = set()
inputfile = fileinput.FileInput()
for line in inputfile:
	words.add(line.rstrip())

palindroms = [w for w in words if w == w[::-1]]

result = [w for w in words if w not in palindroms and w[::-1] in words]

print(sorted(result))
