
from django.contrib.auth.models import User
from django.db import models
from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name='user',
                                related_name='profile')

    @property
    def display_name(self):
        return self.user.get_full_name() or self.user.username