#include <Python.h>
#include <object.h> 

/**
 * print_python_list_info - Prints information about a Python list.
 * @p: A PyObject pointer to the Python list object.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;
    PyListObject *list = (PyListObject *)p; 

    /* List Length */
    size = PyList_Size(list);  

    /* Allocated Space */
    allocated = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    /* Element Types */
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(list, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
