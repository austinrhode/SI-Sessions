from django.shortcuts import render
from .models import Week
from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    weeks = Week.objects.all()
    return render(request, 'main/home.html', {'weeks': weeks, 'title': 'Homepage'})


@login_required
def get_session(request, number):
    week = Week.objects.filter(number=number).first()
    session = week.session
    return render(request, 'main/session.html', {'session': session, 'title': session.title})


class MyLoginView(auth_views.LoginView):
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": "Login"})
        return context
