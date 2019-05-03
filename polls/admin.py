from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None                               , {'fields': ['question_text']}),
        ('Date that publish(past or future)', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
