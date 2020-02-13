from markdown import markdown as md
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

EXTENSIONS = getattr(settings, 'MARKDOWN_EXTENSIONS', [])
register = template.Library()

@register.simple_tag(takes_context=True)
def eval(context, expr):
    result = template.Template(expr).render(context)
    return mark_safe(md(result, extensions=EXTENSIONS))
