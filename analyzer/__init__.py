import argparse

from analyzer import Lexer, SyntaxTree, AnalyticalTable, Validation
from analyzer.output import HTML

output_types = {
    "html": lambda table: HTML.defautl_html_template % HTML.convert(table)
}


def build(expression):
        tokens = Lexer.lex(expression)

        Validation.validate_tokens(tokens)

        tree = SyntaxTree.create(tokens)
        return AnalyticalTable.build(tree)


def main():
    parser = argparse.ArgumentParser(description='Builds analytical table for logical expression.')

    parser.add_argument("expression", metavar="expression",
                        help="logical expression")

    parser.add_argument("-t", "--type", dest="output_type", metavar="output_type",
                        choices=output_types.keys(), default="html",
                        help="output type, can be: " + (', '.join(output_types.keys())))

    args = parser.parse_args()
    table = build(args.expression)
    output_string = output_types[args.output_type](table)

    print(output_string)