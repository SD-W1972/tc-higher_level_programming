#!/usr/bin/python3
""" Read file module """


def read_file(filename=""):
    """
    Read file function

    Prints the content of the provided
    file, otherwise raises an exception
 
    Args:
        filename: string

    Returns:
        Nothing
    """    
    try:
        with open(filename, 'r', encoding='utf-8')as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("file doesn't exist")
    except PermissionError:
        print("file permission")
