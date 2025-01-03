from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Problem

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Problem

from django.shortcuts import render
from .models import Problem, Submission

@login_required
def problem_list(request):
    user = request.user

    # Пайдаланушы шешкен есептерді алу
    solved_problems = Submission.objects.filter(user=user, is_correct=True).values_list('problem_id', flat=True)

    # Шешілмеген есептерді көрсету
    problems = Problem.objects.filter(grade=user.grade).exclude(id__in=solved_problems)

    return render(request, 'problems/problems.html', {'problems': problems})
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Problem, Submission
from django.contrib.auth.decorators import login_required


from django.shortcuts import redirect
from django.contrib import messages
from .models import Problem, Submission

@login_required
def submit_answer(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    user = request.user

    # Бұрын шешілгенін тексеру
    if Submission.objects.filter(user=user, problem=problem, is_correct=True).exists():
        messages.error(request, "Сіз бұл есепті бұрын дұрыс шештіңіз. Қайтадан балл ала алмайсыз.")
        return redirect('problems:problem_list')

    if request.method == 'POST':
        answer = request.POST.get('answer')

        # Дұрыс жауапты тексеру
        is_correct = answer.strip() == problem.correct_answer.strip()
        Submission.objects.create(user=user, problem=problem, submitted_answer=answer, is_correct=is_correct)

        if is_correct:
            user.score += 100  # Тек бірінші рет шешкен кезде 100 балл қосылады
            user.save()

            messages.success(request, "Жауабыңыз дұрыс! 100 балл қосылды.")
        else:
            messages.error(request, "Жауабыңыз қате. Қайта көріңіз.")

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
