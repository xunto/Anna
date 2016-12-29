# -*- coding: utf-8 -*-

from ..AnalyticalTable import Table

default_style_template = '''
    .scope {
        display: table-cell;

        white-space: nowrap;

        padding-right: 5px;
        border-top: solid 1px black;
    }

    .scope + .scope {
        border-left: solid 1px black;
        padding-left: 5px;
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
<code>
{data}
</code>
</body>
</html>
'''


def convert(table):
    return '<div class=\"scope\">' \
           + ('<br/>'.join(str(data) for data in table.data)) \
           + '<br/>' \
           + ''.join(convert(child) for child in table.children) \
           + '</div>'
