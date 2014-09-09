__author__ = 'xixin'


from django.http import HttpResponseRedirect
from django.conf import settings
from picky.models import User


def login_required(view_f):
    def new_view_f(request, *args, **kwargs):
        if 'userid' in request.session:
            return view_f(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return new_view_f


def boss_required(view_f):
    def new_view_f(request, *args, **kwargs):
        if 'userid' in request.session:
            u = User.objects.get(id=request.session['userid'])
            if u.role == 1:
                return view_f(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(settings.LOGIN_URL)
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return new_view_f