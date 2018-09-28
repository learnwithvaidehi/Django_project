from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from enquiry.forms import EnquiryForm

class EnquiryView(CreateView):
    form_class = EnquiryForm
    template_name = "formview.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')