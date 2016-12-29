# -*- coding: utf-8 -*-

from . import Lexer, SyntaxTree, AnalyticalTable, Validation, Brackets


# arguments: string
# returns: table
def build(expression):
    tokens = Lexer.lex(expression)
    tokens = Brackets.restore(tokens)
    Validation.validate_tokens(tokens)
    tree = SyntaxTree.create(tokens)
    table = AnalyticalTable.build(tree)
    return table
