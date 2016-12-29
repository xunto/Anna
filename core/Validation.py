# -*- coding: utf-8 -*-

from . import Tokens


# arguments: list of Token instances
# returns: list of Token instances
def validate_tokens(tokens):
    result = True

    open_brackets = 0

    for token in tokens:
        if isinstance(token, Tokens.OpenGroupToken):
            open_brackets += 1
        elif isinstance(token, Tokens.CloseGroupToken):
            open_brackets -= 1

    if open_brackets != 0:
        raise ValueError('Amount of opened parenthesises doesn\'t match amount of closed ones.')

    return result
