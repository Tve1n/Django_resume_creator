from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ResumeForm
from .models import Resume


def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_success')
    else:
        form = ResumeForm()
    
    return render(request, 'resume/resume_form.html', {'form': form})


def resume_view(request):
    # Получаем последнее добавленное резюме
    resume = Resume.objects.last()
    if not resume:
        return HttpResponse("Резюме еще не создано")
    
    return render(request, 'resume/resume_view.html', {'resume': resume})


def resume_success(request):
    # Cтраница успеха
    return render(request, 'resume/success.html')


def resume_list(request):
    # Список всех резюме, с конца
    resumes = Resume.objects.all().order_by('-created_at')
    return render(request, 'resume/resume_list.html', {'resumes': resumes})


def resume_detail(request, pk):
    # Страница конкретного резюме
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume/resume_view.html', {'resume': resume})