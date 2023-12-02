#!/usr/bin/python3
from head import add,sub
import dis
if __name__ == "__main__":
	def magic_calculation(a, b):

		if a < b:
			c = add(a, b)
			for i in range(4,6):
				c += i
		else:
			return (sub(a,b))
dis.dis(magic_calculation)

