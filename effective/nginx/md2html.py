#coding=utf8

"""
Markdown to html
"""

import sys
import markdown


def md2html(mdstr):
    """
    将mdstr转换成html
    """
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite',
            'markdown.extensions.tables', 'markdown.extensions.toc']

    html = '''
<html lang="zh-cn">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<link href="default.css" rel="stylesheet">
<link href="markdown.css" rel="stylesheet">
</head>
<body>
    %s
</body>
</html>
'''

    ret = markdown.markdown(mdstr, extensions=exts)
    return html % ret


def md2html_file(md_filename, html_filename):
    """
    将md文件转换成html文件
    """

    infile = open(md_filename, 'r')
    md_str = infile.read()
    infile.close()

    outfile = open(html_filename, 'w')
    input_str = unicode(md_str, 'utf-8')
    output_str = md2html(input_str)
    outfile.write(output_str.encode('utf-8'))
    outfile.close()


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print 'Usage: md2html md_filename html_file'
        sys.exit()

    md2html_file(sys.argv[1], sys.argv[2])
