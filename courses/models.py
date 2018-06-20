from django.conf import settings
from django.urls import reverse
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    course_image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        order_with_respect_to = 'date'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail',
        args=str(self.id))

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    overview = models.TextField()
    lesson = models.TextField()
    lesson_number = models.IntegerField()
    lesson_notes = models.TextField()

    class Meta:
        order_with_respect_to = 'lesson_number'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson_detail',
        args=str(self.id))

class Media(models.Model):
    title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=5)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    notes = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('media_detail',
        args=str(self.id))

class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    lesson = models.ForeignKey(
        'Lesson',
        on_delete=models.CASCADE,
    )

    class Meta:
        order_with_respect_to = 'date'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('comment_detail',
        args=str(self.id))