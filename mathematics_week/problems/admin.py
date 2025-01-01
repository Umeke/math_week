from django.contrib import admin
from .models import Problem, Submission

# admin.py
from django.contrib import admin
from .models import Problem

from django.contrib import admin
from .models import Problem

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('question', 'grade', 'admin_only', 'created_at')  # Админде көрсетілетін бағандар
    list_filter = ('grade', 'admin_only')  # Фильтр арқылы іздеу
    search_fields = ('question',)  # Есеп мәтіні бойынша іздеу

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'problem', 'submitted_answer', 'is_correct', 'timestamp')
    list_filter = ('is_correct', 'timestamp')  # Фильтрлер
    search_fields = ('user__username', 'problem__question')  # Пайдаланушы және сұрақ бойынша іздеу
