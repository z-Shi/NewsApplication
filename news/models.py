from django.db import models
from django.utils import timezone


class Story(models.Model):
    MAX_HEADING_LENGTH = 128
    MAX_CONTENT_LENGTH = 512

    heading = models.CharField(max_length=MAX_HEADING_LENGTH)
    content = models.CharField(max_length=MAX_CONTENT_LENGTH)
    publication_date = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.last_visit = timezone.now()
        super(Story, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.heading
