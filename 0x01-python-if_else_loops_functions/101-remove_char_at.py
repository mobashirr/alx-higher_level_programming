#!/usr/bin/python3

def remove_char_at(str, n):

	if(str[n] is not None):
		str = str.replace(str[n],"")

	return(str)
