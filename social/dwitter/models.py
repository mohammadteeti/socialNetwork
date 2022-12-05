from django.db import models

# Create your models here.
# dwitter/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Dweet(models.Model):
    user = models.ForeignKey(User, related_name="dweets", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )

    def __str__(self) -> str:
        return self.user.username + " Profile"

    """for follow and unfollow operations of profile/<int:pk>
    page we have to avoid double submissins using redirect
    as the redirection relates to a profile model
    we can use get_absolute_url() method to redirect to the same
    profile on which the follow/unfollow operation was done
    see ( profile view )"""

    def get_absolute_url(self):
        return "/profile/%i" % self.user.id


# ...
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


# Create a Profile for each new user.
# post_save.connect(create_profile, sender=User)
print(post_save)
