from django.db import models
from django.utils.html import mark_safe



class MediaUser(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    image = models.ImageField(null=True, default='default.png')

    def image_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="70" height="70" />' % (self.image))

    image_tag.short_description = 'Image'
    
    def __str__(self) -> str:
        return self.last_name


class Post(models.Model):
    owner = models.ForeignKey(MediaUser, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png')
    text = models.TextField()
    def image_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="70" height="70" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.owner.first_name
