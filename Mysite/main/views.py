from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail, get_connection
from django.conf import settings

from .forms import ContactForm
from .models import Hello

class HelloListAndFormView(SuccessMessageMixin,ListView,FormView):
    model = Hello #get data from db
    template_name = 'main.html'
    context_object_name = 'list_projects'
    queryset = Hello.objects.all().order_by('-pub_date')
    object_list = None

    form_class = ContactForm
    success_url = '/'
    success_message = 'Form successfully submitted!'

    def form_valid(self,form):
        cd = form.cleaned_data
        con = get_connection('django.core.mail.backends.console.EmailBackend')
        send_mail (
            cd['name'],
            cd['message'],
            cd.get('email', 'noreply@example.com'),
            ['info.meshackkimwele@gmail.com'],
            fail_silently=False
        )
        return super(HelloListAndFormView, self).form_valid(form)