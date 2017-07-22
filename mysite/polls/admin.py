from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['questionText']}),
        ('Data information', {'fields': ['pubDate'], 'classes': ['collapse']}),
    ]

    list_display = ('questionText', 'pubDate', 'was_published_recently')

    inlines = [ChoiceInline]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
