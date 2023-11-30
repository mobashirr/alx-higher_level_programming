#!/usr/bin/python3
(lambda f, x: print(f(f, x)))(lambda self, c: chr(c) + self(self, c + 1) if c < ord('Z') else chr(c), ord('A'))
