#!/usr/bin/python3
def multiple_returns(frase):
    l = len(frase)
    c = frase[0] if l > 0 else None
    t = (l, c)
    return t
