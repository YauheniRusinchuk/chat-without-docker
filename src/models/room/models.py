from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Room(models.Model):
    ''' Модель создания комнаты  '''
    founder         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='founder_room')
    name            = models.CharField(max_length=255, blank=False)
    password        = models.CharField(max_length=255, blank=False)
    slug            = models.SlugField()
    participants 	= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users_in_room')
    create_date     = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('main:room:detail_room', kwargs={'slug': self.slug, 'pk': self.pk})

    def get_delete_room(self):
        return reverse('main:room:delete_room', kwargs={'slug': self.slug, 'pk': self.pk})


    def __str__(self):
        return f"Комната {self.name}"


    class Meta:
        ordering = ['-create_date']



def pre_save_room_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    instance.slug = slug


pre_save.connect(pre_save_room_receiver, sender=Room)
