'''
View classes building HTTP responses for URLS
'''
from typing import Any
from django.views.generic import TemplateView


class HomeView(TemplateView):
    '''View class for MrED home page'''
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        '''Grabs context and sends to home.html'''

        # Empty for now
        context = super().get_context_data(**kwargs)

        return context

class SignInView(TemplateView):
    '''View class for sign in page'''
    template_name = "sign-in.html"

    def get_context_data(self, **kwargs):
        '''Grabs context and sends to sign-in.html'''

        # Empty for now
        context = super().get_context_data(**kwargs)

        return context
    
class TriageResultView(TemplateView):
    '''View class for triage result page'''
    template_name = "triage-result.html"

    def get_context_data(self, **kwargs):
        '''Grabs context and sends to triage-result.html'''

        # Empty for now
        context = super().get_context_data(**kwargs)

        return context
    
class NotificationSentView(TemplateView):
    '''View class for notification sent page'''
    template_name = "notification-sent.html"

    def get_context_data(self, **kwargs):
        '''Grabs context and sends to notification-sent.html'''

        # Empty for now
        context = super().get_context_data(**kwargs)

        return context
