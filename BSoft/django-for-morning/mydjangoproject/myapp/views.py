import datetime

from myapp.forms import LoginForm
from django.shortcuts import render
from myapp.models import Facebook


def login(request):
    status = "not saved"
    if request.method == "POST":
        login_form_object = LoginForm(request.POST, request.FILES)
        if login_form_object.is_valid():
            fb_obj = Facebook()
            fb_obj.name = login_form_object.cleaned_data['username']
            request.session["username"] = login_form_object.cleaned_data['username']
            fb_obj.picture = login_form_object.cleaned_data['picture']
            fb_obj.save()
            status = "Saved"
    else:
        login_form_object = LoginForm()

    response = render(request, 'myapp/template/login.html', {"status": status})
    last_log = datetime.datetime.now()
    response.set_cookie('last_login', last_log)
    return response


def view_dashboard(request):
    session_user = request.session['username']
    cookie_user = request.COOKIES['username']
    last_login = request.COOKIES['last_login']
    last_log_time = datetime.datetime.strptime(last_login[:-7], "%Y-%m-%d %H:%M:%S")
    return render(request, 'myapp/template/dashboard.html', {"s_username": session_user, "c_username": cookie_user, "last_log": last_log_time})
