'''
View classes building HTTP responses for URLS
'''
from typing import Any
from django.views.generic import TemplateView


class MapView(TemplateView):
    '''Main map page'''
    template_name = "map.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''Grabs data and sends to map.html'''
        context = super().get_context_data(**kwargs)
        coordinates = [[]]


        context['coordinates'] = coordinates
        return context
