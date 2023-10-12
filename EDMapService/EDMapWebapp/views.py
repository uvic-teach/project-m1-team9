'''
View classes building HTTP responses for URLS
'''
import csv
from typing import Any
from django.views.generic import TemplateView


class MapView(TemplateView):
    '''Main map page'''
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        '''Grabs data and sends to map.html'''

        context = super().get_context_data(**kwargs)
        coordinates = []

        # Open csv
        with open('edcoordinates.csv',
                newline='',
                encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                coordinates.append([row['hospitalname'], row['latitude'], row['longitude']])
            
        if (coordinates):
            print(f"{len(coordinates)} coordinates loaded and ready for the map library!\n")

        context['coordinates'] = coordinates
        return context
