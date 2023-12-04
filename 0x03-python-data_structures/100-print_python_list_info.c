#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t pythonlist = PyList_Size(p),
    alocated = ((PyListObject *)p)->allocated,
    index = 0;
    PyObject *object;

    /*size of the object */
    printf("[*] Size of the Python List = %zd\n", pythonlist);
    /* memory allocated */
    printf("[*] Allocated = %zd\n", alocated);

    /*print the elements of an opject*/
    for (; index < pythonlist; index++)
    {
        object = PyList_GET_ITEM(p, index);
        printf("Element %zd: %s\n", index, object->ob_type->tp_name);
    }
}