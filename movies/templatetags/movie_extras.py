from django import template

register = template.Library()

@register.filter
def average(queryset, field_name):
    values = [getattr(obj, field_name, 0) for obj in queryset]
    return sum(values) / len(values) if values else 0