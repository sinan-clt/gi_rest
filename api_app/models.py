from django.db import models



# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Notes"

