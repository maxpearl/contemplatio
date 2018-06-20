from django.contrib import admin
from . import models

class CommentInline(admin.TabularInline):
    model = models.Comment

class LessonAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(models.Course)
admin.site.register(models.Comment)
admin.site.register(models.Lesson, LessonAdmin)
admin.site.register(models.Media)
