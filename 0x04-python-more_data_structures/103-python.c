void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;

    // Type check (Add error message if it fails)
    if (!PyBytes_Check(p)) { 
        fprintf(stderr, "[.] Invalid Bytes Object\n");
        return;
    }

    // Direct size access 
    printf("  size: %ld\n", *((long *)((char *)bytes + 20))); 

    // Print bytes, handling non-printables as hex 
    printf("  trying string: ");
    for (int i = 0; i < bytes->ob_size && i < 10; i++) {
        char byte = ((char *)bytes + 32)[i]; 
        if (isprint(byte))
            putchar(byte);
        else
            printf("%02x ", (unsigned char)byte); 
    }
    printf("\n");
}
