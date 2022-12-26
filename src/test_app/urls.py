from django.urls import path

from test_app.views import base

urlpatterns = [
    path('', base, {'name': 'home'}, name='home'),
    path('level1_1/', base, {'name': 'Уровень1_1'}, name='level1_1'),
    path('level1_2/', base, {'name': 'Уровень1_2'}, name='level1_2'),
    path(
        'level1_1/level1_1_1', base,
        {'name': 'Уровень1.1.1'}, name='level1.1.1'
    ),
    path(
        'level1_1/level1_1_2', base,
        {'name': 'Уровень1.1.2'}, name='level1.1.2'
    ),
    path(
        'level1_1/level1_1_1/level1_1_1_1', base,
        {'name': 'Уровень1.1.1.1'}, name='level1.1.1.1'
    ),
]
