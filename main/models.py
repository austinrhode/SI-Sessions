from django.db import models
from PIL import Image


class Session(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Week(models.Model):
    number = models.IntegerField()
    image = models.ImageField(default='default.png', upload_to='session_images')
    topic = models.CharField(max_length=200)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)

