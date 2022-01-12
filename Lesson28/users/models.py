from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
User = get_user_model()

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_num = models.IntegerField(null=True, blank=True)
	sex = models.BooleanField(default=None, null=True, blank=False)  # True=male False=Female Default=None
		

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)
    
	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

	def __str__(self) -> str:
		return f"{self.user.username} - {self.user.first_name} {self.user.last_name}"
