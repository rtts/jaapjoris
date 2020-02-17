from datetime import date
from django.utils import timezone
from cms.forms import ContactForm
from cms.views import SectionView, SectionFormView
from cms.decorators import register_view

from .models import *

@register_view(TextSection)
class TextView(SectionView):
    template_name = 'app/sections/text.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        then = date(1983, 6, 6)
        now = timezone.now()
        context['age'] = now.year - then.year - ((now.month, now.day) < (then.month, then.day))
        return context

@register_view(ImageSection)
class ImageView(SectionView):
    template_name = 'app/sections/image.html'

@register_view(VideoSection)
class VideoView(SectionView):
    template_name = 'app/sections/video.html'

@register_view(ButtonSection)
class ButtonView(SectionView):
    template_name = 'app/sections/button.html'

@register_view(ContactSection)
class ContactFormView(SectionFormView):
    form_class = ContactForm
    success_url = '/thanks/'
    template_name = 'app/sections/contact.html'
