#include <Python.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t pythonlist = PyList_Size(p),
    alocated = ((PyListObject *)p)->allocated,
    i = 0;
    PyObject *object;

    /*size of the object */
    printf("[*] Size of the Python List = %zd\n", pythonlist);
    /* memory allocated */
    printf("[*] Allocated = %zd\n", alocated);

    /*print the elements of an opject */
    for (; i < pythonlist; i++)
    {
        object = PyList_GET_ITEM(p, i);
        printf("Element %zd: %s\n", i, object->ob_type->tp_name);
    }
}