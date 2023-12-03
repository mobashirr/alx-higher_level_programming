#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

	i = len(tuple_a)
	j = len(tuple_b)

	a = tuple_a[0] if i >= 1 else 0
	b = tuple_a[1] if i >= 1 else 0
	a = tuple_a[0] if j >= 1 else 0
	b = tuple_a[1] if j >= 1 else 0

	if i > 1 and j >= 1:
		a = tuple_a[0] + tuple_b[0]
	if i > 1 and j >= 2:
		b = tuple_a[1] + tuple_b[1]

	tuple = (a, b)
	return (tuple)


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

