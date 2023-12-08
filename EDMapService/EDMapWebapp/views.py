'''
View classes building HTTP responses for URLS. 
Each class corresponds to a different starting location.
'''
import csv
from django.views.generic import TemplateView

class VictoriaView(TemplateView):
    '''Strategy design pattern class to generate data for Victoria'''
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        '''Grabs data and sends to map.html'''

        context = super().get_context_data(**kwargs)
        coordinates = []

        # Parse coordinates from csv
        with open('edcoordinates.csv',
                newline='',
                encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                coordinates.append([row['hospitalname'], row['latitude'], row['longitude']])

        context['coordinates'] = coordinates
        # Set view coordinate to Victoria
        context['view_coordinate'] = [48.429, -123.357]
        return context

class SidneyView(TemplateView):
    '''Strategy design pattern class to generate data for Sidney'''
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        '''Grabs data and sends to map.html'''

        context = super().get_context_data(**kwargs)
        coordinates = []

        # Parse coordinates from csv
        with open('edcoordinates.csv',
                newline='',
                encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                coordinates.append([row['hospitalname'], row['latitude'], row['longitude']])

        context['coordinates'] = coordinates
        # Set view coordinate to Sidney
        context['view_coordinate'] = [48.6502, -123.3990]
        return context

class NanaimoView(TemplateView):
    '''Strategy design pattern class to generate data for Nanaimo'''
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        '''Grabs data and sends to map.html'''

        context = super().get_context_data(**kwargs)
        coordinates = []

        # Parse coordinates from csv
        with open('edcoordinates.csv',
                newline='',
                encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                coordinates.append([row['hospitalname'], row['latitude'], row['longitude']])

        context['coordinates'] = coordinates
        # Set view coordinate to Nanaimo
        context['view_coordinate'] = [49.1659, -123.9401]
        return context

class VancouverView(TemplateView):
    '''Strategy design pattern class to generate data for Vancouver'''
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        '''Grabs data and sends to map.html'''

        context = super().get_context_data(**kwargs)
        coordinates = []

        # Parse coordinates from csv
        with open('edcoordinates.csv',
                newline='',
                encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                coordinates.append([row['hospitalname'], row['latitude'], row['longitude']])

        context['coordinates'] = coordinates
        # Set view coordinate to Vancouver
        context['view_coordinate'] = [49.2827, -123.1207]
        return context
