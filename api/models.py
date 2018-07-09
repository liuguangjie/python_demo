from django.db import models

# Create your models here.


class User(models.Model):

    class Meta:
        db_table = 'sys_user'

    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=50)
