#!/usr/bin/python3
"""
Text identation module
This module provides a function tha identates the 
provided string on its conducts
"""

def text_indentation(text):
    """
    Prints the provided string and identates it by
    breaking a line if it finds a character that's equal
    to "," ":" or "?"

    Args:
        text: string
    
    Raises:
        TypeError: if text is not a str object

    Returns:
        Nothing
    """

    if not isinstance(text, str):
        raise(TypeError("text must be a string"))

    text = text.strip()
    for i in range(0, len(text)):
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n\n" ,end="")
