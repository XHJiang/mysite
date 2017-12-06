from django.contrib import admin

# Register your models here.
from .models import Publisher, Book, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('authors',)
    date_hierarchy = 'publication_date'
    ordering = ('publication_date',)
    # filter_horizontal = ('authors',)

admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)