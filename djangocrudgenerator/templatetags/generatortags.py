# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.simple_tag
def gen_url_tag(*args, **kwargs):
    """ Helper Template tag that generates an url tag:
         {% url "the:url:path" %}
    """
    _kwargs = reduce(lambda i, k: i+u'%s="%s" ' % (k, kwargs[k]), kwargs, u'')
    return u'{%% url "%s" %s %%}' % (u":".join(args), _kwargs)


@register.simple_tag
def start_tag():
    return u"{%"


@register.simple_tag
def end_tag():
    return u"%}"


@register.simple_tag
def start_var():
    return u"{{"


@register.simple_tag
def end_var():
    return u"}}"


@register.simple_tag
def start_comment():
    return u"{#"


@register.simple_tag
def end_comment():
    return u"#}"
