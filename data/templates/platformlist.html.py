# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1413135930.534446
_enable_loop = True
_template_filename = '/home/dan/eval/evalproject/templates/platformlist.html'
_template_uri = '/platformlist.html/'
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
    return runtime._inherit_from(context, u'/base.html/', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <ul>\n')
        # SOURCE LINE 5
        for platform in c.platforms:
            # SOURCE LINE 6
            __M_writer(u'        <li><a href="platforms/')
            __M_writer(escape(platform.id))
            __M_writer(u'">')
            __M_writer(escape(platform.name))
            __M_writer(u'</a></li>\n')
        # SOURCE LINE 8
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<h1>Platform List</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


