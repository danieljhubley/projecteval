# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409716413.318625
_enable_loop = True
_template_filename = '/home/austinvalle/EValProject/evalproject/templates/game.html'
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
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <p>\n        Description: ')
        __M_writer(escape(c.game.desc))
        __M_writer(u'\n    </p>\n    <p>\n        Release Date: ')
        __M_writer(escape(c.game.release_date.date()))
        __M_writer(u'\n    </p>\n    <p>\n        Developer: ')
        __M_writer(escape(c.game.developer))
        __M_writer(u'\n    </p>\n    <p>\n        Publisher: ')
        __M_writer(escape(c.game.publisher))
        __M_writer(u'\n    </p>\n    <p>\n        Trailer: ')
        __M_writer(escape(c.game.trailer_url))
        __M_writer(u'\n    </p>\n    <a href="#" onclick="window.history.back()">Go Back</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <h1>')
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
        __M_writer(escape(c.game.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 3, "34": 6, "40": 7, "45": 7, "46": 9, "47": 9, "48": 12, "49": 12, "50": 15, "51": 15, "52": 18, "53": 18, "54": 21, "55": 21, "61": 4, "66": 4, "67": 5, "68": 5, "69": 5, "70": 5, "76": 3, "81": 3, "87": 81}, "uri": "/game.html/", "filename": "/home/austinvalle/EValProject/evalproject/templates/game.html"}
__M_END_METADATA
"""
