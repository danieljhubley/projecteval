# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1413141425.269918
_enable_loop = True
_template_filename = '/home/dan/eval/evalproject/templates/platform.html'
_template_uri = '/platform.html/'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['body', 'css_link', 'heading', 'innercss', 'title']


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
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(u'\n')
        # SOURCE LINE 43
        __M_writer(u'\n\n')
        # SOURCE LINE 49
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n    <p>\n        Description: ')
        # SOURCE LINE 12
        __M_writer(escape(c.platform.desc))
        __M_writer(u'\n    </p>\n    <p>\n        Release Date: ')
        # SOURCE LINE 15
        __M_writer(escape(c.platform.release_date.date()))
        __M_writer(u'\n    </p>\n    <p>\n        Developer: ')
        # SOURCE LINE 18
        __M_writer(escape(c.platform.developer))
        __M_writer(u'\n    </p>\n    <p>\n        CPU: ')
        # SOURCE LINE 21
        __M_writer(escape(c.platform.cpu))
        __M_writer(u'\n    </p>\n    <p>\n        Memory: ')
        # SOURCE LINE 24
        __M_writer(escape(c.platform.memory))
        __M_writer(u'\n    </p>\n    <p>\n        Graphics: ')
        # SOURCE LINE 27
        __M_writer(escape(c.platform.graphics))
        __M_writer(u'\n    </p>\n    <p>\n        Storage: ')
        # SOURCE LINE 30
        __M_writer(escape(c.platform.storage))
        __M_writer(u'\n    </p>\n    <p>\n        Available Games:\n        <div class="game-content">\n\t        <ul>\n')
        # SOURCE LINE 36
        for game in c.games:
            # SOURCE LINE 37
            __M_writer(u'\t\t        <li><a href="/games/')
            __M_writer(escape(game.id))
            __M_writer(u'">')
            __M_writer(escape(game.title))
            __M_writer(u'</a></li>\n')
        # SOURCE LINE 39
        __M_writer(u'\t        </ul>\n        </div>\n    </p>\n    <a href="" onclick="window.history.go(-1); return false;">Go Back</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css_link(context,path,media=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\n')
        # SOURCE LINE 46
        if path not in self.seen_css:
            # SOURCE LINE 47
            __M_writer(u'\t\t<link rel="stylesheet" type="text/css" href="')
            __M_writer(filters.html_escape(escape(path)))
            __M_writer(u'" media="')
            __M_writer(escape(media))
            __M_writer(u'"></link>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    <h1>')
        # SOURCE LINE 8
        __M_writer(escape(c.platform.id))
        __M_writer(u' - ')
        __M_writer(escape(c.platform.name))
        __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_innercss(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def css_link(path,media=''):
            return render_css_link(context,path,media)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\t')
        # SOURCE LINE 3
        __M_writer(escape(css_link('/static/css/game-list.css', 'screen')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(escape(c.platform.name))
        return ''
    finally:
        context.caller_stack._pop_frame()


