#!/usr/bin/python3
(lambda f, x: (lambda s, c: print(s(s, c)))(lambda self, c: chr(c) + self(self, c + (c < ord('Z')) - (c == ord('Z'))), x))(lambda f, x: (lambda s, c: print(s(s, c)))(lambda self, c: chr(c) + self(self, c + (c < ord('Z')) - (c == ord('Z'))), x))
