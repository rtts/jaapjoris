import cms
from datetime import date
from django.utils import timezone
from cms.forms import ContactForm

@cms.register('Tekst')
class TextSection(cms.SectionView):
    fields = ['content']
    template_name = 'app/sections/text.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        then = date(1983, 6, 6)
        now = timezone.now()
        context['age'] = now.year - then.year - ((now.month, now.day) < (then.month, then.day))
        return context

@cms.register('Afbeelding')
class ImageSection(cms.SectionView):
    fields = ['image']
    template_name = 'app/sections/image.html'

@cms.register('Contact')
class ContactSection(cms.SectionFormView):
    fields = ['title']
    form_class = ContactForm
    success_url = '/thanks/'
    template_name = 'app/sections/contact.html'
