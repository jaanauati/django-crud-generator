# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.simple_tag
def gen_url_tag(*args, **kwargs):
    """ Helper Template tag that generates an url tag:
         {% url "the:url:path" %}
    """
    if len(args) == 0:
        raise template.TemplateSyntaxError(
            "gen_url_tag require one o more arguments.")
    _kwargs = reduce(lambda i, k: i+u'%s="%s" ' % (k, kwargs[k]), kwargs, u'')
    return u'{%% url "%s" %s %%}' % (u":".join(args), _kwargs[:-1])


#TODO: use Django-1.5 {% template 'ananan' %} instead of the followin functios.
#https://docs.djangoproject.com/en/dev/ref/templates/builtins/#templatetag
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
