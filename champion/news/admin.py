from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_content', 'created_at']
    list_display_links = ['short_content', 'title']
    exclude = ['slug']
    search_fields = ('title', 'content')

    @admin.display(description="Описание")
    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    