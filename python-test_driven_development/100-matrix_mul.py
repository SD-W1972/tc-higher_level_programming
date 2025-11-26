#!/usr/bin/python3
"""
Matrix multiplication module
This module provides a function to
multiply to matrices
"""

def matrix_mul(m_a, m_b):
    """
    This function multiplies m_a and m_b with
    multiple validation patterns

    Args:
        m_a: matrix a (float or integer)
        m_b: matrix b (float or integer)
    
    Raises:
        TypeError: if m_a or m_b aren't lists
        TypeError: if m_a or m_b aren't matrices
        ValueError: if m_a or m_b are empty
        TypeError: if m_a or m_b contains numbers that aren't
        floats or integers
        TypeError: if the number of rows isn't even on m_a or m_b
        ValueError: if m_a and m_b can't be multiplied
    """
    if(not isinstance(m_a, list) or
        not isinstance(m_b, list)):
        raise(TypeError
        ("m_a must be a list or m_b must be a list"))
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError
        ("m_a must be a list of lists or m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0:
        raise(ValueError
        ("m_a can't be empty or m_b can't be empty"))
    for row in m_a:
        for element in row:
            if not isinstance(element, (float, int)):
                raise(TypeError
                ("m_a should contain only integers or floats or m_b should contain nly integers or floats"))
    for row in m_b:
        for element in row:
            if not isinstance(element, (float, int)):
                raise
            (TypeError("m_a should contain only integers or floats or m_b should contain nly integers or floats"))

    row_size = len(m_a[0])
    if not all(len(row) == row_size for row in m_a):
        raise
    (TypeError("each row of m_a must be of the same size or each row of m_b ust be of the same size"))
    row_sizeb = len(m_b[0])
    if not all(len(row) == row_size for row in m_b):
        raise
    (TypeError("each row of m_a must be of the same size or each row of m_b ust be of the same size"))

    if row_size != row_sizeb:
        raise(ValueError
        ("m_a and m_b can't be multiplied"))

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
