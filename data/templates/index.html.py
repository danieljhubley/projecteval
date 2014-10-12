# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1413148220.343108
_enable_loop = True
_template_filename = '/home/dan/eval/evalproject/templates/index.html'
_template_uri = '/index.html/'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['body', 'innerjs', 'heading']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html/', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 14
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    <div class="search">\n\t    <input type="text" id="search-text-box" name="search-text-box" class="search-text-box" value="" />\n        <button id="search-button" class="search-button">Search</button>\n    </div>\n    <div id="results">\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_innerjs(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n    <script type="text/javascript" src="/static/javascript/home.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'<h1>Main Page</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


