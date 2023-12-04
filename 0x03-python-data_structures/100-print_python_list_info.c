#include <Python.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t pythonlist = PyList_Size(p),
    aloc = ((PyListObject *)p)->allocated,
    index = 0;
    PyObject *object;

    printf("[*] Size of the Python List = %zd\n", pythonlist);
    printf("[*] Allocated = %zd\n", aloc);
    for (; index < pythonlist; index++)
    {
        object = PyList_GET_ITEM(p, index);
        printf("Element %zd: %s\n", index, object->ob_type->tp_name);
    }
}