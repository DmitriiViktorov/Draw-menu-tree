from django.core.management.base import BaseCommand
from draw_app.models import Menu, MenuItem

class Command(BaseCommand):
    """Команда для заполнения базы данных начальными значениями"""
    help = 'Fill db with some start data'

    def handle(self, *args, **options):
        titles = ['Menu_01', 'Menu_02', 'Menu_03']
        levels_prefix = {
            1: 'level',
            2: 'sublevel',
            3: 'category',
            4: 'subcategory',
        }

        for menu_title in titles:
            Menu.objects.get_or_create(title=menu_title)

        def create_menu_items(menu, parent=None, current_level=1, max_level=4):

            if current_level > max_level:
                return

            for i in range(1, 4):
                title_prefix = parent.title if parent else menu.title
                title = f'{title_prefix}_{levels_prefix[current_level]}_{i}'
                menu_item, _ = MenuItem.objects.get_or_create(menu=menu, title=title, parent=parent)
                create_menu_items(menu, parent=menu_item, current_level=current_level + 1, max_level=max_level)

        for menu in Menu.objects.all():
            create_menu_items(menu)

        self.stdout.write(self.style.SUCCESS('Database successfully filled with initial data.'))
