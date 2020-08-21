from django.db import models


class Post(models.Model):
    post_type = models.BooleanField()
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    post_time = models.DateTimeField()

    class Meta:
        ordering = ['-post_time']

    def votescore(self):
        return self.up_votes - self.down_votes