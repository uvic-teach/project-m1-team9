'''
View classes building HTTP responses for URLS
'''
from django.views.generic import TemplateView


class HomeView(TemplateView):
    '''View class for MrED home page'''
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        '''Grabs context and sends to map.html'''

        # Empty for now
        context = super().get_context_data(**kwargs)

        return context
