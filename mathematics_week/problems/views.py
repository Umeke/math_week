from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Problem

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Problem

@login_required
def problem_list(request):
    problems = Problem.objects.filter(grade=request.user.grade, admin_only=False).exclude(solved_by=request.user)
    return render(request, 'problems/problems.html', {'problems': problems})


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Problem, Submission
from django.contrib.auth.decorators import login_required


@login_required
def submit_answer(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)

    if request.method == "POST":
        user_answer = request.POST.get('answer', '').strip()

        # Тексеру: дұрыс жауап па?
        is_correct = str(user_answer) == problem.correct_answer

        # Жауапты сақтау
        submission = Submission.objects.create(
            user=request.user,
            problem=problem,
            submitted_answer=user_answer,
            is_correct=is_correct
        )

        # Дұрыс жауап болса, балл қосу
        if is_correct:
            request.user.score += 100  # 100 балл қосу
            request.user.save()
            messages.success(request, "Дұрыс жауап! Сізге 100 балл қосылды.")
        else:
            messages.error(request, "Қате жауап. Қайта көріңіз.")

        return redirect('problems:problem_list')


from django.shortcuts import render
from users.models import CustomUser

from django.shortcuts import render


def leaderboard_view(request):
    grades = range(5, 12)  # 5-сыныптан 11-сыныпқа дейін
    leaderboard_data = {}

    for grade in grades:
        users_in_grade = CustomUser.objects.filter(grade=grade).order_by('-score')
        leaderboard_data[f"{grade}"] = users_in_grade

    return render(request, 'problems/leaderboard.html', {'leaderboard': leaderboard_data})
