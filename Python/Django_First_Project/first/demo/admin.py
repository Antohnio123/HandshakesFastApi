from django.contrib import admin
from .models import Book, BookNumber, Character, Author


# admin.site.register(Book)
# простой способ отобразить таблицу. Настраиваемый способ - через класс.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'price', 'published', 'is_published']
    list_display = ['title', 'price', 'is_published']
    list_filter = ['published']
    search_fields = ['title', 'description', 'published']


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)