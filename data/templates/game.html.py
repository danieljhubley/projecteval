# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1413135932.655775
_enable_loop = True
_template_filename = '/home/dan/eval/evalproject/templates/game.html'
_template_uri = '/game.html/'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['body', 'heading', 'title']


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
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    <p>\n        Description: ')
        # SOURCE LINE 9
        __M_writer(escape(c.game.desc))
        __M_writer(u'\n    </p>\n    <p>\n        Release Date: ')
        # SOURCE LINE 12
        __M_writer(escape(c.game.release_date.date()))
        __M_writer(u'\n    </p>\n    <p>\n        Developer: ')
        # SOURCE LINE 15
        __M_writer(escape(c.game.developer))
        __M_writer(u'\n    </p>\n    <p>\n        Publisher: ')
        # SOURCE LINE 18
        __M_writer(escape(c.game.publisher))
        __M_writer(u'\n    </p>\n    <p>\n        Trailer: <a href="')
        # SOURCE LINE 21
        __M_writer(escape(c.game.trailer_url))
        __M_writer(u'">')
        __M_writer(escape(c.game.trailer_url))
        __M_writer(u'</a>\n    </p>\n    <a href="" onclick="window.history.go(-1); return false;">Go Back</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    <h1>')
        # SOURCE LINE 5
        __M_writer(escape(c.game.id))
        __M_writer(u' - ')
        __M_writer(escape(c.game.title))
        __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(escape(c.game.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


