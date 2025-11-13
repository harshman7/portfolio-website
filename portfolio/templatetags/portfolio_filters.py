from django import template

register = template.Library()


@register.filter
def mul(value, arg):
    """Multiply the value by the argument"""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def contains_tech(tech_list, search_term):
    """Check if tech list contains a search term (case-insensitive)"""
    if not tech_list:
        return False
    search_lower = search_term.lower()
    return any(search_lower in str(tech).lower() for tech in tech_list)

