'''
View classes building HTTP responses for URLS
'''
from django.views.generic import TemplateView


class MapView(TemplateView):
    '''Main map page'''
    template_name = "map.html"
