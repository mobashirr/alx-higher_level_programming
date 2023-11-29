#!/usr/bin/python3

def remove_char_at(str, n):

	if(n < len(str) and n >= 0):
		new = str.replace(str[n],"")

	return(new)
