from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.http import HttpResponse

from django.conf import settings

def yandex_verification(request):
  html_content = """
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        </head>
        <body>
            Verification: 4570bd092af176b8
        </body>
    </html>"""
  return HttpResponse(html_content, content_type='text/html; charset=utf-8')

urlpatterns = [

    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('administrator/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('timetable/', include('timetable.urls')),
    path('reviews/', include('reviews.urls')),
    path('payment/', include('payment.urls')),
    path('booking/', include('booking.urls')),
    path('yandex_4570bd092af176b8.html', yandex_verification),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
