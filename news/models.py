from django.db import models

#бд с новостями
class News(models.Model):
    title = models.CharField(max_length=50)
    anons = models.CharField(max_length=250)
    full_text = models.TextField(blank='True')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/articles/{self.id}'