#include <stdio.h>
#include "/usr/bin/python3.10"

/**
 * print_python_list_into
 * @p: object
*/
void print_python_list_info(PyObject *p)
{

	int size_o = PyObject_Size(p);

	printf("[*] Size of the Python List = %d\n", size_o);
	


}