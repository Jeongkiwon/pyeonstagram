
from django.views.generic.base import TemplateView
from member.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from main import settings
@login_required()
def login_yet(request):
    return redirect('post:index')

def home(request):
    return render(request, 'home.html')

def user_list(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'user_list.html', context)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)