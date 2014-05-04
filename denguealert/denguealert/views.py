from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response
from django.conf import settings

from denguealert.forms import DengueCaseForm

class ReportView(TemplateView):
    template_name = 'report.html'

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super(ReportView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        # context = super(ReportView, self).get_context_data(**kwargs)
        # context['form'] = DengueCaseForm()
        extra_context = {
            'form': DengueCaseForm(),
            'GMAPS_API_KEY': settings.GMAPS_API_KEY}
        return render_to_response(self.template_name, extra_context)
