#coding=utf8

"""
Fast Cgi Server
"""

import os.path

from flup.server.fcgi import WSGIServer
from md2html import md2html


def myapp(environ, start_response):
    """
    myapp
    """

    # 确保正确处理中文
    filepath = environ['SCRIPT_FILENAME'].decode('utf-8')

    if not os.path.exists(filepath):
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return ['404 Not Found!\n']

    if filepath[-3:] == '.md':
        start_response('200 OK', [('Content-Type', 'text/html')])
        infile = open(filepath, 'r')
        md_str = infile.read()
        infile.close()
        input_str = unicode(md_str, 'utf-8')
        output_str = md2html(input_str)
        return [output_str.encode('utf-8')]
    else:
        start_response('200 OK', [('Content-Type', 'text/plain')])
        infile = open(filepath, 'r')
        file_str = infile.read()
        infile.close()
        return [file_str]


if __name__ == '__main__':
    WSGIServer(myapp, bindAddress=('127.0.0.1', 8008)).run()
