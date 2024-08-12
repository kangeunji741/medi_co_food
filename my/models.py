from django.db import models
from django.contrib.auth.models import User

class SocialProfile(models.Model):
    user = models.AutoField(User,primary_key=True, db_comment='아이디')
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username