"""
View classes for all possible section types.
"""

from datetime import date
from typing import Any

from cms.decorators import section_view
from cms.views import ContactSectionFormView, SectionView
from django.utils import timezone


@section_view
class TextSection(SectionView):
    """
    A section that displays text.
    """

    verbose_name = "Tekst"
    fields = ["content"]
    template_name = "text.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """
        Insert age into context.
        """

        # Calculate my age.
        then = date(1983, 6, 6)
        now = timezone.now()
        age = now.year - then.year - ((now.month, now.day) < (then.month, then.day))

        return super().get_context_data(age=age, **kwargs)


@section_view
class ImageSection(SectionView):
    """
    A section that displays an image.
    """

    verbose_name = "Afbeelding"
    fields = ["image"]
    template_name = "image.html"


@section_view
class ContactSection(ContactSectionFormView):
    """
    A section that displays a contact form.
    """

    verbose_name = "Contact"
    fields = ["content", "href", "subject"]
    template_name = "contact.html"
