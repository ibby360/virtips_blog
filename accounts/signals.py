# Core Django imports.
from django.db.models.signals import post_save
from django.dispatch import receiver

# Blog and Accounts application imports.
from accounts.models import Account
from blog.models import Author

# Creates author profile immediately an account is created for her/him.
@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)


# Saves author profile automatically after creating the profile.
@receiver(post_save, sender=Account)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
