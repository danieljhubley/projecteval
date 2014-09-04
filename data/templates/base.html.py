# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409720145.236439
_enable_loop = True
_template_filename = u'/home/austinvalle/EValProject/evalproject/templates/base.html'
_template_uri = u'/base.html/'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['head', 'footer', 'title', 'css_link', 'header', 'nav', 'heading', 'css']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        set = context.get('set', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n\t')
        self.seen_css = set()
        
        __M_writer(u'\n\t<head>\n    \t<title>')
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    \t')
        __M_writer(escape(self.head()))
        __M_writer(u'\n\t</head>\n\t<body>\n    \t')
        __M_writer(escape(self.header()))
        __M_writer(u'\n    \t')
        __M_writer(escape(self.nav()))
        __M_writer(u'\n    \t')
        __M_writer(escape(self.heading()))
        __M_writer(u'\n    \t')
        __M_writer(escape(next.body()))
        __M_writer(u'\n    \t')
        __M_writer(escape(self.footer()))
        __M_writer(u'\n\t</body>\n</html>\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\t')
        __M_writer(escape(self.css()))
        __M_writer(u'\n\n\t<script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'EVal Project')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css_link(context,path,media=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if path not in self.seen_css:
            __M_writer(u'\t\t<link rel="stylesheet" type="text/css" href="')
            __M_writer(filters.html_escape(escape(path)))
            __M_writer(u'" media="')
            __M_writer(escape(media))
            __M_writer(u'"></link>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n\t<div>\n\t\t<header><a href="/"><span>EVal Project</span></a></header>\n\t\t<nav>\n\t\t\t<ul>\n\t\t\t\t<li><a href="/games">Games</a></li>\n\t\t\t\t<li><a href="/platforms">Platforms</a></li>\n\t\t\t</ul>\n\t\t</nav>\n\n\t\t<div>\n\t\t\t<!--Login will go here-->\n\t\t</div>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def css_link(path,media=''):
            return render_css_link(context,path,media)
        __M_writer = context.writer()
        __M_writer(u'\n\t')
        __M_writer(escape(css_link('/static/css/eval.css', 'screen')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 44, "134": 51, "140": 51, "141": 52, "142": 52, "16": 0, "148": 142, "24": 2, "25": 3, "27": 3, "28": 5, "29": 5, "30": 6, "31": 6, "32": 9, "33": 9, "34": 10, "35": 10, "36": 11, "37": 11, "38": 12, "39": 12, "40": 13, "41": 13, "42": 17, "43": 23, "44": 26, "45": 42, "46": 45, "47": 49, "48": 53, "54": 19, "59": 19, "60": 20, "61": 20, "67": 47, "71": 47, "77": 17, "81": 17, "87": 55, "92": 55, "93": 56, "94": 57, "95": 57, "96": 57, "97": 57, "98": 57, "104": 25, "108": 25, "114": 28, "118": 28, "124": 44}, "uri": "/base.html/", "filename": "/home/austinvalle/EValProject/evalproject/templates/base.html"}
__M_END_METADATA
"""
