# -*- coding: utf-8 -*-

from ..AnalyticalTable import Table

default_style_template = '''
        .table .scope {
            display: table-cell;
            white-space: nowrap;
            border-top: solid 1px black;
            padding-right: 5px;
        }

        .table .scope + .scope {
            padding-left: 5px;
            border-left: solid 1px black;
        }

        .table>.scope {
            border: none;
        }

        .table {
            font-family: monospace;
            background: #e0e0e0;
            margin-top: 10px;
            padding: 10px;
            border-radius: 10px;
            overflow-x: scroll;
        }
'''

default_html_template = '''
<!DOCTYPE html>
<html>
<head>
<style>
{style}
</style>
</head>
<body>
<div class="table">
{data}
</div>
<div style="clear:both"></div>
</body>
</html>
'''


def convert(table):
    return '<div class=\"scope\">' \
           + ('<br/>'.join(str(data) for data in table.data)) \
           + '<br/>' \
           + ''.join(convert(child) for child in table.children) \
           + '</div>'
