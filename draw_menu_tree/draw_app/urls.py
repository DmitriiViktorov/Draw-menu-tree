from django.urls import path, re_path
from .views import index, draw_menu

urlpatterns = [
    path('', index, name='index'),
    # path('<path:path>/', draw_menu, name='menu_tree'),
    path('menu/<str:main_menu>/<str:current_menu>/', draw_menu, name='menu'),
    path('menu/<str:main_menu>/', draw_menu, name='menu'),
]