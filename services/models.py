from django.db import models
from users.models import User

class Service(models.Model):
    service_provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)