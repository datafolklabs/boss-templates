
from django.contrib.auth.models import User
from django.db import models
from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name='user',
                                related_name='profile')
