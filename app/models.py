from django.db import models
from django.conf import settings
from cms.models import BasePage, BaseSection

class Page(BasePage):
    '''Add custom fields here. Already existing fields: position, title,
    slug, menu

    '''

class Section(BaseSection):
    '''Add custom fields here. Already existing fields: type, position,
    title, content, image, video, button_text, button_link

    '''
    color = models.PositiveIntegerField('kleur', default=1, choices=settings.SECTION_COLORS)
