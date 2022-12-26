from typing import Any, Dict, List

from django import template
from django.db.models import QuerySet
from django.template import RequestContext
from django.urls import NoReverseMatch, reverse

from menu_app.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(
    context: RequestContext, menu_name: str = '', parent_id: int = 0
) -> Dict[str, Any]:
    """Custom template tag to generate menu on the site.

    Args:
        context (RequestContext): request context
        menu_name (str, optional): name of certain menu. Defaults to ''.
        parent_id (int, optional): id for parent menu. Defaults to 0.

    Returns:
        Dict[str, Any]: context for generating menu inside the template
    """

    if parent_id != 0 and 'menu' in context:
        menu = context['menu']
    else:
        current_path = context['request'].path
        menu = _get_menu(current_path, menu_name)

    return {
        'menu': menu,
        'active_menu': (item for item in menu if item['parent'] == parent_id),
    }


def _get_menu(current_path: str, menu_slag: str = '') -> List[Dict[str, Any]]:
    """Generates list of dicts for menu drawing.

    Args:
        current_path (str): current relative url.
        menu_slag (str, optional): unique menu name. Defaults to ''.

    Returns:
        List[Dict[str, Any]]: list with every menu item in dict format.
    """
    menu = []
    menu_data = MenuItem.objects.select_related(
        ).filter(menu__slug=menu_slag).order_by('pk')

    for item in menu_data:
        relative_item_path = item.path.strip()

        try:
            url = reverse(relative_item_path)
        except NoReverseMatch:
            url = _get_url(item, relative_item_path, menu_data)
            root_url = current_path.split('/')[1]
            url = '/' + root_url + url if root_url else url

        menu.append({
            'id': item.pk,
            'url': url,
            'name': item.name,
            'parent': item.parent_id or 0,
            'active': True if url == current_path else False,
        })

    return menu


def _get_url(item: MenuItem, item_path: str, menu_data: QuerySet) -> str:
    """Creates full url path for every menu item.

    Args:
        item (MenuItem): current menu item
        item_path (str): current menu item's relative path
        menu_data (QuerySet): queryset with all menu items

    Returns:
        str: full item path except for app name
    """
    path = item_path
    parent_item = menu_data.get(pk=item.parent_id)

    while parent_item.parent_id:
        path = parent_item.path.strip() + '/' + path
        parent_item = menu_data.get(pk=parent_item.parent_id)

    path = '/' + parent_item.path.strip() + '/' + path
    return path
