from django.db import models
from datetime import datetime
from django.contrib.auth.models import User  # in order to use django admin standard users table

class Note(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(null = False)
    pinned = models.BooleanField(blank = True, null = True)
    date_created = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        db_table = 'Note'

    def __str__(self):
        return self.title

    # not necessary, just formatting date and time to look pretty (and brazilian)
    def getCreationDate(self):
        return self.date_created.strftime('%d/%m/%Y @ %H:%M')
