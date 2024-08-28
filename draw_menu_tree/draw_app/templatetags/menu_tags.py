from typing import List

from django import template
from django.urls import resolve
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, main_menu, menu_structure):
    """
    Тег для отрисовки меню в выбранном месте шаблона.

    Parameters:
        context: Контекст шаблона Django
        main_menu: Название главного меню для отрисовки
        menu_structure: Древовидная структура меню, которая будет отрисована

    Returns:
        Словарь с данными для использования в шаблоне draw_menu.html
    """
    return { 'main_menu': main_menu, 'menu_structure': menu_structure}