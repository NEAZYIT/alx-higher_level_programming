#include "Python.h"
#include <stdio.h>
#include <float.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints information about Python list, such as size and
 * the amount of memory allocated. It also prints the type of each element,
 * and if the element is of type 'bytes' or 'float', additional information
 * about the element is printed.
 *
 * @p: Pointer to a Python object.
 *
 * Return: void.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t p_size;
	Py_ssize_t idx;
	PyObject *n;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		p_size = PyList_Size(p);
		printf("[*] Size of the Python List = %zd\n", p_size);
		printf("[*] Allocated = %zd\n", ((PyListObject *)(p))->allocated);
		for (idx = 0; idx < p_size; idx++)
		{
			n = PyList_GetItem(p, idx);
			printf("Element %zd: %s\n", idx, Py_TYPE(n)->tp_name);
			if (PyBytes_Check(n))
				print_python_bytes(n);
			else if (PyFloat_Check(n))
				print_python_float(n);
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
	fflush(stdout);
}

/**
 * print_python_bytes - Checks if the object is a Python bytes object. If so,
 * it prints the size, attempts to print it as a string, and prints the first
 * 10 bytes in hexadecimal.
 *
 * @p: Pointer to a Python object.
 *
 * Return: void.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t p_size;
	Py_ssize_t idx;
	Py_ssize_t max;
	char *str;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		p_size = PyBytes_Size(p);
		str = PyBytes_AsString(p);
		printf("  size: %zd\n  trying string: %s\n", p_size, str);
		if (p_size < 10)
			max = p_size + 1;
		else
			max = 10;
		printf("  first %zd bytes: ", max);
		for (idx = 0; idx < max; idx++)
			printf("%02x ", (unsigned char)str[idx]);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
	fflush(stdout);
}

/**
 * print_python_float - Checks if the object is a Python float object. If so,
 * it prints the float value. If it is not, it prints an error message.
 *
 * @p: Pointer to a Python object.
 *
 * Return: void.
 */

void print_python_float(PyObject *p)
{
	PyObject *convert;

	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		convert = PyObject_Repr(p);
		convert = PyUnicode_AsEncodedString(convert, "utf-8", "~E~");
		printf("  value: %s\n", PyBytes_AsString(convert));
		Py_XDECREF(convert);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
	fflush(stdout);
}
