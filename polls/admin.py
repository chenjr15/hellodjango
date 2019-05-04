from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # 'classes':['collapse'] 指明这个选项可以折叠起来
    fieldsets = [
        (None                               , {'fields': ['question_text']}),
        ('Date that publish(past or future)', {'fields': ['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
