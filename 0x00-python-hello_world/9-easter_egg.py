#!/usr/bin/python3
import io
import contextlib

with io.StringIO() as buf, contextlib.redirect_stdout(buf):
    import this
    zen = buf.getvalue()

# Print the Zen of Python
print(f"{zen[:34]}\n{zen[35:]}")