import re
import sys

from . import Tokens

token_definitions = [
    # {
    #     'regex': re.compile(r'!'),
    #     'class': Tokens.InversionToken
    # },
    {
        'regex': re.compile(r'&'),
        'class': Tokens.ConjunctionToken
    },
    {
        'regex': re.compile(r'\|'),
        'class': Tokens.DisjunctionToken
    },
    {
        'regex': re.compile(r'->'),
        'class': Tokens.ImplicationToken
    },
    {
        'regex': re.compile(r'<->'),
        'class': Tokens.EquivalenceToken
    },
    {
        'regex': re.compile(r'\('),
        'class': Tokens.OpenGroupToken
    },
    {
        'regex': re.compile(r'\)'),
        'class': Tokens.CloseGroupToken
    },
    {
        'regex': re.compile(r'[a-zA-Z0-9]+'),
        'class': Tokens.VariableToken
    },
]


def lex(expression):
    pos = 0
    tokens = []

    while pos < len(expression):
        token = None

        for token_definition in token_definitions:
            match = token_definition['regex'].match(expression, pos)
            if match is not None:
                token = token_definition['class']()
                if isinstance(token, Tokens.VariableToken):
                    token.name = match.group(0)

                pos = match.end(0)
                break

        if token is None:
            raise ValueError("Unexpected symbol at %d." % pos)
        else:
            tokens.append(token)

    return tokens
