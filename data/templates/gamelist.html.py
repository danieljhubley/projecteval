# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409716314.269519
_enable_loop = True
_template_filename = '/home/austinvalle/EValProject/evalproject/templates/gamelist.html'
_template_uri = '/gamelist.html/'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['body', 'heading']


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
        __M_writer(u'\n    <ul>\n')
        for game in c.games:
            __M_writer(u'        <li><a href="games/')
            __M_writer(escape(game.id))
            __M_writer(u'">')
            __M_writer(escape(game.title))
            __M_writer(u'</a></li>\n')
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'<h1>Game List</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 1, "33": 2, "67": 61, "39": 3, "44": 3, "45": 5, "46": 6, "47": 6, "48": 6, "49": 6, "50": 6, "51": 8, "57": 2, "27": 0, "61": 2}, "uri": "/gamelist.html/", "filename": "/home/austinvalle/EValProject/evalproject/templates/gamelist.html"}
__M_END_METADATA
"""
