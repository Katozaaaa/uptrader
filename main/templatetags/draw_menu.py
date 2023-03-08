from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu(menu_dict):
    menu_html = ''
    path_to_parent_section = ''
    for section in menu_dict.items():
        if section[1]:
            if section[0] != 'main':
                path_to_parent_section += section[0] + '/'
            menu_html += render_to_string(
                'sections/menu.html', 
                context={'section_block_id': section[0], 'path_to_parent_section': path_to_parent_section, 'sections': section[1]}
            )
    return mark_safe(menu_html)