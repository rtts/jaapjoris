from datetime import date
from django.utils import timezone
from django.http import HttpResponse

from cms.views import SectionView, SectionFormView
from cms.decorators import section_view
from cms.forms import ContactForm

@section_view
class TextSection(SectionView):
    verbose_name = 'Tekst'
    fields = ['content']
    template_name = 'text.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        then = date(1983, 6, 6)
        now = timezone.now()
        context['age'] = now.year - then.year - ((now.month, now.day) < (then.month, then.day))
        return context

@section_view
class ImageSection(SectionView):
    verbose_name = 'Afbeelding'
    fields = ['image']
    template_name = 'image.html'

@section_view
class ContactSection(SectionFormView):
    verbose_name = 'Contact'
    fields = ["content", "href"]
    form_class = ContactForm
    template_name = 'contact.html'

    def form_valid(self, form):
        response = HttpResponse(status=302)
        response["Location"] = form.save(self.object.href)
        return response
