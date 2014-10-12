# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1413144375.246245
_enable_loop = True
_template_filename = u'/home/dan/eval/evalproject/templates/base.html'
_template_uri = u'/base.html/'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['head', 'innercss', 'footer', 'title', 'css_link', 'header', 'nav', 'innerjs', 'heading', 'css']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        set = context.get('set', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<html>\n\t')
        # SOURCE LINE 3
        self.seen_css = set()
        
        __M_writer(u'\n\t<head>\n    \t<title>')
        # SOURCE LINE 5
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    \t')
        # SOURCE LINE 6
        __M_writer(escape(self.head()))
        __M_writer(u'\n\t</head>\n\t<body>\n    \t')
        # SOURCE LINE 9
        __M_writer(escape(self.header()))
        __M_writer(u'\n    \t')
        # SOURCE LINE 10
        __M_writer(escape(self.nav()))
        __M_writer(u'\n\t')
        # SOURCE LINE 11
        __M_writer(escape(self.heading()))
        __M_writer(u'\n\t')
        # SOURCE LINE 12
        __M_writer(escape(next.body()))
        __M_writer(u'\n\t')
        # SOURCE LINE 13
        __M_writer(escape(self.footer()))
        __M_writer(u'\n\t</body>\n</html>\n\n')
        # SOURCE LINE 17
        __M_writer(u'\n\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        __M_writer(u'\n\n')
        # SOURCE LINE 46
        __M_writer(u'\n\n')
        # SOURCE LINE 50
        __M_writer(u'\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n\n')
        # SOURCE LINE 58
        __M_writer(u'\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n\t')
        # SOURCE LINE 20
        __M_writer(escape(self.css()))
        __M_writer(u'\n\n\t<script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>\n    ')
        # SOURCE LINE 23
        __M_writer(escape(self.innerjs()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_innercss(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'EVal Project')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css_link(context,path,media=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 60
        __M_writer(u'\n')
        # SOURCE LINE 61
        if path not in self.seen_css:
            # SOURCE LINE 62
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
        # SOURCE LINE 26
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n\t<div class="nav-bar">\n\t\t<header><a href="/"><img src="/pylons-logo.gif" /></a></header>\n\t\t<nav>\n\t\t\t<ul>\n\t\t\t\t<li><a href="/games">Games</a></li>\n\t\t\t\t<li><a href="/platforms">Platforms</a></li>\n\t\t\t</ul>\n\t\t</nav>\n\n\t\t<div>\n\t\t\t<!--Login will go here-->\n\t\t</div>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_innerjs(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 66
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def css_link(path,media=''):
            return render_css_link(context,path,media)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer(u'\n\t')
        # SOURCE LINE 53
        __M_writer(escape(css_link('/static/css/eval.css', 'screen')))
        __M_writer(u'\n\t')
        # SOURCE LINE 54
        __M_writer(escape(self.innercss()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


