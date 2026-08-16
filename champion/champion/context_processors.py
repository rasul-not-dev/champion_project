def nav_links(request):
    return {
        'nav_links': [
            {'title': 'главная', 'url_name': 'home', 'icon': 'fa-solid fa-house'},
            {'title': 'новости', 'url_name': 'news', 'icon': 'fa-solid fa-pen'},
            {'title': 'расписание', 'url_name': 'home', 'icon': 'fa-solid fa-calendar-days'},
            {'title': 'оплата', 'url_name': 'home', 'icon': 'fa-solid fa-tag'},
            {'title': 'отзывы', 'url_name': 'home', 'icon': 'fa-solid fa-star'},
        ]
    }

def social_media_icons(request):
    return {
        'social_media_icons': [
            {'title': 'макс', 'url_name': '#', 'icon': 'fa-brands fa-discourse'},
            {'title': 'инстаграмм', 'url_name': '#', 'icon': 'fa-brands fa-square-instagram'},
            {'title': 'телеграмм', 'url_name': '#', 'icon': 'fa-brands fa-telegram'},
            {'title': 'вконтакте', 'url_name': '#', 'icon': 'fa-brands fa-vk'},
        ]
    }