#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about Python lists
 * @p: Pointer to the Python list object
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_size(p)p;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *tyoe = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, type);
	}
}
