from core import Lexer, SyntaxTree, AnalyticalTable, Validation


def build(expression):
    tokens = Lexer.lex(expression)
    Validation.validate_tokens(tokens)
    tree = SyntaxTree.create(tokens)
    table = AnalyticalTable.build(tree)
    return table