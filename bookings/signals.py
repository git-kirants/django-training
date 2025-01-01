from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
from django.core.mail import send_mail

@receiver(post_save, sender=Booking)
def send_booking_confirmation(sender, instance, created, **kwargs):
    if created and instance.status == 'confirmed':
        send_mail(
            'Booking Confirmed',
            f'Your booking for {instance.service.title} has been confirmed.',
            'noreply@example.com',
            [instance.gardener.email],
        )
