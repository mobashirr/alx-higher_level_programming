#include "/usr/include/python3.8.10"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

/**
 * print_python_list_info - print and modifypy list in c
 * @p: PyObject which is python list
 * Return: NULL
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;
	PyObject *obj;
	PyListObject *ll;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		ll = (PyListObject *)obj;
		printf("%s\n", ll->ob_base.ob_base.ob_type);
	}

}
