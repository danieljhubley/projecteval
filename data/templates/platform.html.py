# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1409719664.616837
_enable_loop = True
_template_filename = '/home/austinvalle/EValProject/evalproject/templates/platform.html'
_template_uri = '/platform.html/'
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
        __M_writer(escape(c.platform.desc))
        __M_writer(u'\n    </p>\n    <p>\n        Release Date: ')
        __M_writer(escape(c.platform.release_date.date()))
        __M_writer(u'\n    </p>\n    <p>\n        Developer: ')
        __M_writer(escape(c.platform.developer))
        __M_writer(u'\n    </p>\n    <p>\n        CPU: ')
        __M_writer(escape(c.platform.cpu))
        __M_writer(u'\n    </p>\n    <p>\n        Memory: ')
        __M_writer(escape(c.platform.memory))
        __M_writer(u'\n    </p>\n    <p>\n        Graphics: ')
        __M_writer(escape(c.platform.graphics))
        __M_writer(u'\n    </p>\n    <p>\n        Storage: ')
        __M_writer(escape(c.platform.storage))
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
        __M_writer(escape(c.platform.id))
        __M_writer(u' - ')
        __M_writer(escape(c.platform.name))
        __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(escape(c.platform.name))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 3, "34": 6, "40": 7, "45": 7, "46": 9, "47": 9, "48": 12, "49": 12, "50": 15, "51": 15, "52": 18, "53": 18, "54": 21, "55": 21, "56": 24, "57": 24, "58": 27, "59": 27, "65": 4, "70": 4, "71": 5, "72": 5, "73": 5, "74": 5, "80": 3, "85": 3, "91": 85}, "uri": "/platform.html/", "filename": "/home/austinvalle/EValProject/evalproject/templates/platform.html"}
__M_END_METADATA
"""
