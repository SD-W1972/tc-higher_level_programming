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
        error_msg = str(e)
        # Converter mensagens do NumPy para o formato esperado
        if "matmul" in error_msg or "shapes" in error_msg:
            raise ValueError("m_a and m_b can't be multiplied")
        raise ValueError(error_msg)
    except TypeError as e:
        error_msg = str(e)
        # String não é operando válido
        if "operand" in error_msg or "scalar" in error_msg.lower():
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        raise TypeError(error_msg)
    except Exception as e:
        raise
