#!/usr/bin/python3

def remove_char_at(str, n):

	i = n
	if(i < len(str) and  i >= 0):
		new = str.replace(str[n],"")

	return(new)
