from django.contrib import admin
from .models import Question, Answer

# with the help of tabular in line , we have the opportunity to add answer below the questions
class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)