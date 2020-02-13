from django.db import models
from django.conf import settings
from cms.models import BasePage, BaseSection
from cms.decorators import register_model

class Page(BasePage):
    '''Add custom fields here. Already existing fields: position, title,
    slug, menu

    '''

class Section(BaseSection):
    '''Add custom fields here. Already existing fields: type, position,
    title, content, image, video, button_text, button_link

    '''
    color = models.PositiveIntegerField('kleur', default=1, choices=settings.SECTION_COLORS)

@register_model('Tekst')
class TextSection(Section):
    fields = ['title', 'content']
    class Meta:
        proxy = True

@register_model('Button')
class ButtonSection(Section):
    fields = ['button_text', 'button_link']
    class Meta:
        proxy = True

@register_model('Afbeelding')
class ImageSection(Section):
    fields = ['title', 'image']
    class Meta:
        proxy = True

@register_model('Video')
class VideoSection(Section):
    fields = ['title', 'video']
    class Meta:
        proxy = True

@register_model('Contact')
class ContactSection(Section):
    fields = ['title']
    class Meta:
        proxy = True
