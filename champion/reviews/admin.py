from django.contrib import admin
from .models import Reviews

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_comment', 'rating', 'created_at']
    list_display_links = ['name', 'short_comment']
    exclude = ['created_at']
    search_fields = ['name']

    @admin.display(description='комментарий')
    def short_comment(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment


