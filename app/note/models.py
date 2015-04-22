from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Note(models.Model):
    user = models.ForeignKey('auth.User')
    pub_date = models.DateTimeField('date created', default=timezone.now)
    title = models.CharField(max_length=200)
    body = models.TextField()

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ('-pub_date',)
        verbose_name_plural = 'notes'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note:detail', args=[str(self.id)])
