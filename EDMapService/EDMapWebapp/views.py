'''
View classes building HTTP responses for URLS
'''
import csv
from typing import Any
from django.views.generic import TemplateView


class MapView(TemplateView):
    '''Main map page'''
    template_name = "map.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''Grabs data and sends to map.html'''
        context = super().get_context_data(**kwargs)
        coordinates = [[]]

        with open('EDMapService/EDMapData/HospitalList.csv',
                newline='',
                encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['hospitalname'], row['latitude'], row['longitude'])

        context['coordinates'] = coordinates
        return context
