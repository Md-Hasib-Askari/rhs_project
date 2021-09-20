from django.db import models

# Create your models here.
class IPAddress(models.Model):
    ip_address = models.TextField(blank=True, max_length=200)
    visited_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_address
