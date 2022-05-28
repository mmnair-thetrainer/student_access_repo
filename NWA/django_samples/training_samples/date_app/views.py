from django.http import HttpResponse

def date_app(request,name):
    value = "Hello %s" % name
    return HttpResponse(value)