import argparse

from core import Lexer, SyntaxTree, AnalyticalTable
from core.output import HTML


# tokens = Lexer.lex("(A->(B->A))")
# tokens = Lexer.lex("((A->B)->((A->(B->C))->(A->C))")
# tokens = Lexer.lex("((!A))->(B->(A&B)))")
# tokens = Lexer.lex("(A->B)")
tokens = Lexer.lex("(A<->B)")

print('tokens:   ', tokens)
tree = SyntaxTree.create(tokens)
print('syntax tree:', tree.to_json())

table = AnalyticalTable.build(tree)
print('table:', table.to_json())

print('html:', HTML.convert(table))