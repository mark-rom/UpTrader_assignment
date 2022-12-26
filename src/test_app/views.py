from django.shortcuts import render


def base(request, name):
    return render(request, 'test_app/nav_bar.html', {'name': name})
