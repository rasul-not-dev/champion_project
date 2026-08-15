def nav_links(request):
    return {
        'nav_links': [
        {'title': 'главная', 'url_name': 'home', 'icon': 'fa-solid fa-house'},
        {'title': 'расписание', 'url_name': 'home', 'icon': 'fa-solid fa-calendar-days'},
        {'title': 'оплата', 'url_name': 'home', 'icon': 'fa-solid fa-tag'},
        {'title': 'отзывы', 'url_name': 'home', 'icon': 'fa-solid fa-star'},
    ]
    }