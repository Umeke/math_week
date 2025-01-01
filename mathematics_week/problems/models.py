from datetime import timezone
from django.utils import timezone
from django.db import models

from django.db import models

class Problem(models.Model):
    question = models.CharField(max_length=255)  # Есептің мәтіні
    correct_answer = models.CharField(max_length=255)  # Есептің дұрыс жауабы
    grade = models.IntegerField(  # Сынып деңгейін көрсету үшін
        choices=[(i, f"{i}-сынып") for i in range(5, 12)],  # 5-11 сынып
        default=5
    )
    admin_only = models.BooleanField(default=False)  # Админге ғана көрінетін есептер
    created_at = models.DateTimeField(auto_now_add=True)  # Есептің құрылу күні
    image = models.ImageField(upload_to='problem_images/', blank=True, null=True)  # Сурет үшін өріс

    def __str__(self):
        return f"{self.question} ({self.grade}-сынып)"


class Submission(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='submissions')
    submitted_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'problem')  # Бір пайдаланушы бір есепті бір рет қана шеше алады

    def __str__(self):
        return f"{self.user.username} - {self.problem.question}"