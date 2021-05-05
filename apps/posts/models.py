from django.db import models

class post (models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

class comment (models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        to=post,on_delete=models.CASCADE, related_name='post_comments'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text

