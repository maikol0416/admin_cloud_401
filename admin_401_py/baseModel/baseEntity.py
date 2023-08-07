from django.db import models
import uuid

STATUS_CHOICES = (
    ('active','Active'),
    ('disabled', 'Disabled'),
)

class BaseModelShared(models.Model):
    code = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="active")
    
    class Meta:
        abstract = True