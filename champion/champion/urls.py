from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from django.conf import settings

urlpatterns = [

    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('administrator/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('timetable/', include('timetable.urls')),
    path('reviews/', include('reviews.urls')),
    path('payment/', include('payment.urls')),
    path('booking/', include('booking.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
