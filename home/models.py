from django.db import models
#from django.utils.timezone import now

# Create your models here.

class Member(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=256)
    level0 = models.CharField(max_length=10, default=0)
    upLevel_id = models.CharField(max_length=10, null=True, default=None)
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tree_db2'


