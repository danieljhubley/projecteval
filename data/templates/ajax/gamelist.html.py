# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1413147602.421558
_enable_loop = True
_template_filename = '/home/dan/eval/evalproject/templates/ajax/gamelist.html'
_template_uri = '/ajax/gamelist.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<ul>\n')
        # SOURCE LINE 2
        for game in c.games:
            # SOURCE LINE 3
            __M_writer(u'    <li><a href="/games/')
            __M_writer(escape(game.id))
            __M_writer(u'">')
            __M_writer(escape(game.title))
            __M_writer(u'</a></li>\n')
        # SOURCE LINE 5
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


