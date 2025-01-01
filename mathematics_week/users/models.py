from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    score = models.IntegerField(default=0)  # Пайдаланушының ұпайы
    solved_problems = models.ManyToManyField('problems.Problem', blank=True, related_name='solved_by')  # Шешілген есептер
    grade = models.IntegerField(
        choices=[(i, f"{i}-сынып") for i in range(5, 12)],  # 5-11 сынып
        null=True,
        blank=True,
        verbose_name="Сынып"
    )
