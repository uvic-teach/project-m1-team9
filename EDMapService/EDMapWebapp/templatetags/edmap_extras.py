"""Django template extras for edmap microservice"""
from django import template

register = template.Library()


@register.filter
def index(indexable, i):
    """
    Makes it possible to specify an index on a variable within
    the Django html template
    Example:
        {{ list|index:0 }},
    or as found in sites.html:
        {% with bone_count_sums|index:forloop.counter0 as sum %}
        Do something...
        {% endwith %}
    """
    return indexable[i]