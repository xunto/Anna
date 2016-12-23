from analyzer.AnalyticalTable import Table

defautl_html_template = '''
<!DOCTYPE html>
<html>
<head>
<style>
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
</style>
</head>
<body>
<code>
%s
</code>
</body>
</html>
'''


def convert(table: Table):
    return '<div class=\"scope\">' \
           + ('<br/>'.join(str(data) for data in table.data)) \
           + '<br/>' \
           + ''.join(convert(child) for child in table.children) \
           + '</div>'
