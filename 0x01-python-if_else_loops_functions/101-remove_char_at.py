#!/usr/bin/python3

def remove_char_at(str, n):

	i = n if n >= 0 else n * -1
	if(i < len(str)):
		str = str.replace(str[n],"")

	return(str)
