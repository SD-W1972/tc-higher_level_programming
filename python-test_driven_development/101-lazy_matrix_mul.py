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
    """
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError(str(e)) from e
    except Exception as e:
        raise
