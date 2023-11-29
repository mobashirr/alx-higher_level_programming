#!/usr/bin/python3

def remove_char_at(str, n):

	n = n if n >= 0 else n * -1
	if(n < len(str)):
		str = str.replace(str[n],"")

	return(str)
