from django.urls import path
from . import views

app_name = 'problems'

urlpatterns = [
    path('', views.problem_list, name='problem_list'),  # Барлық есептерді көрсету

    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('problems/submit/<int:problem_id>/', views.submit_answer, name='submit_answer'),

]
