#!/usr/bin/python3

def uppercase(str):

	j = 0

	while j < len(str):
        
		i = int.from_bytes(str[j].encode('utf-8'), 'big')

		if 97 <= i <= 122:
			i = i - (97 - 65)

		print("{:c}".format(i), end="")
		j += 1
	print("\n")
