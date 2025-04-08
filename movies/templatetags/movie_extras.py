from django import template

register = template.Library()

@register.filter
def average_rating(ratings):
    if not ratings.exists():
        return "-"
    total = sum(r.score for r in ratings)
    return round(total / ratings.count(), 1)