from django.contrib import admin
from .models import Question, Answer

@admin.register(Question)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Answer)
class AuthorAdmin(admin.ModelAdmin):
    pass
