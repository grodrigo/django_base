from django.contrib import admin

from .models import Question

"""
admin.site.register(Question)


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
"""

#admin.site.register(Choice)

from .models import Choice, Question

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
#    list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['^question_text']
#    search_fields = ['=question_text']

admin.site.register(Question, QuestionAdmin)

""" Para cambiar por ejemplo el titulo
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('My site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()
admin_site.register(Question, QuestionAdmin)

y registrar la url en urls.py:
from polls.admin import admin_site
    url(r'^admin/', include(admin_site.urls)),

pero es mas facil en el urls.py
admin.site.site_header = 'Nombre titulo desde el urls!'
"""
