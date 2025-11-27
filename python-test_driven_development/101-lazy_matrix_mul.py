#!/usr/bin/python3
"""
Lazy matrix multiplication module
This module provides a function to multiply two matrices using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies m_a and m_b using NumPy

    Args:
        m_a: matrix a (float or integer)
        m_b: matrix b (float or integer)

    Returns:
        Result of matrix multiplication as a NumPy array

    Raises:
        ValueError: if matrices cannot be multiplied
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    try:
        a = np.array(m_a)
        b = np.array(m_b)
        result = np.matmul(a, b)
        return result
    except ValueError as e:
        if "aligned" in str(e):
            raise ValueError(str(e)) from e
        raise
    except Exception as e:
        raise
