from core import Tokens


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
