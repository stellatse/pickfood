from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from picky.decorators import login_required


def login(request):
    data = {}
    if 'last_username' in request.COOKIES:
        data['last_username'] = request.COOKIES['last_username']
    return render(request, 'login.html', data)


# @login_required
def home(request):

    return render(request, 'index.html')


def user(request, user_id):
    return render(request, 'user.html')