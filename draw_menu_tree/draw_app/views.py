from typing import Optional

from django.db.models import Q
from django.shortcuts import render

from .models import Menu, MenuItem


def index(request):
    """
    Вью-функция для отрисовки главной страницы.

    На главной странице отображаются все главные разделы меню, которые служат ссылками для отрисовки
    древовидной структуры подпунктов меню.

    Parameters:
    request: объект запроса Django

    Returns:
    HTTP-ответ, рендерящий шаблон 'draw_app/index.html' с контекстом, содержащим
             главные разделы меню.
    """
    menus = Menu.objects.all()
    return render(request, 'draw_app/index.html', {'menus': menus})


def build_menu_structure(menu_items, current_menu):
    """
    Рекурсивно формирует древовидную структуру меню от текущего элемента до корневых элементов.

    Эта функция начинает с текущего элемента меню и рекурсивно строит древовидную структуру, добавляя
    дочерние элементы в виде ключей в структуру меню. Если у текущего элемента есть родитель, функция
    рекурсивно обрабатывает его, пока не достигнет верхнего уровня меню. Если текущий элемент является
    верхним уровнем, функция добавляет все меню верхнего уровня в результирующую структуру.

    Parameters:
        menu_items: Список объектов MenuItem, представляющих все элементы меню.
        current_menu: Название текущего элемента меню, с которого начинается построение структуры.

    Returns:
        Словарь, представляющий древовидную структуру меню от текущего элемента до корневых элементов.
    """
    current_menu_item = next((item for item in menu_items if item.title == current_menu), None)
    tree = {}

    def get_parents(menu_tree, all_menu_list, level):
        """
        Вспомогательная рекурсивная функция для построения дерева меню.

        Parameters:
            menu_tree: Текущее состояние дерева меню.
            all_menu_list: Список всех элементов меню.
            level: Текущий уровень меню для обработки.

        Returns:
            Обновленное состояние дерева меню.
        """
        current_tree = {level: menu_tree}

        children = [x for x in menu_items if x.parent == level]
        if children:
            for child in children:
                if not current_tree[level].get(child):
                    current_tree[level].update({child: {}})

        current_tree[level] = dict(sorted(current_tree[level].items()))

        parent = next((item for item in menu_items if item == level.parent), None)
        if parent:
            return get_parents(current_tree, all_menu_list, parent)

        else:
            top_levels = [x for x in menu_items if x.order == 0 and x != level]
            for top_level in top_levels:
                current_tree[top_level] = {}
            return dict(sorted(current_tree.items()))

    if current_menu_item:
        menu_tree_structure = get_parents(tree, menu_items, current_menu_item)
        return menu_tree_structure
    return tree


def draw_menu(request, main_menu, current_menu: Optional[str] = None):
    """
    Вью функция для отрисовки древовидной структуры меню.

    Если запрос произошел только через название главного меню - шаблон отразит первый уровень
    входящих в него пунктов для возможности отрисовки дальнейшего дерева меню.
    Если запрос произошел через название главного меню и текущее меню - происходит отрисовка
    всего дерева меню от текущего до главного меню.

    Parameters
        request: объект запроса Django
        main_menu: Название текущего меню, до которого требуется отобразить структуру меню.
                         Если не указано, отобразится только первый уровень меню.

    Returns:
        HTTP-ответ, рендерящий шаблон 'draw_app/menu_tree.html' с контекстом, содержащим
             основное меню и структурированное дерево меню.
    """
    if not current_menu:
        queryset = MenuItem.objects.filter(Q(menu__title=main_menu) & Q(order=0)).all()
        menu_structure = {item: {} for item in queryset}
    else:
        queryset = MenuItem.objects.filter(menu__title=main_menu).prefetch_related('parent')
        menu_structure = build_menu_structure(queryset, current_menu)

    return render(request, 'draw_app/menu_tree.html', context={'main_menu': main_menu, 'menu_structure': menu_structure})
