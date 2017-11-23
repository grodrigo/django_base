from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #will display horizontally if you further group them in a tuple:
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


#Add the BookInstance information inline to our Book detail:
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
    can_delete = False

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
#   display_genre function in model because ManyToManyField
#   cuidado estas cosas: display_genre hace un join, ver costos en DB
    list_display = ('title', 'author', 'display_genre')
    # cuidado con estas cosas, no hace una consulta por cada uno?
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
