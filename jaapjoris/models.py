"""
Page and section models.
"""

from cms.decorators import page_model, section_model
from cms.models import BasePage, BaseSection
from django.db import models


@page_model
class Page(BasePage):
    pass


@section_model
class Section(BaseSection):
    page = models.ForeignKey(Page, related_name="sections", on_delete=models.PROTECT)
