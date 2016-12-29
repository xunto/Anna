#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

import core
from core.output import HTML


output_types = {
    "html": lambda table:
        HTML.default_html_template.format(data=HTML.convert(table), style=HTML.default_style_template)
}


def main():
    parser = argparse.ArgumentParser(description='Builds analytical table for logical expression.')

    parser.add_argument("expression", metavar="expression", type=str,
                        help="logical expression, without spaces, actions: \"!, |, &, ->, <->\"")

    parser.add_argument("-t", "--type", dest="output_type", metavar="output_type", type=str,
                        choices=output_types.keys(), default="html",
                        help="output type, can be: " + (', '.join(output_types.keys())))

    args = parser.parse_args()
    table = core.build(args.expression)
    output_string = output_types[args.output_type](table)

    print(output_string)

main()
