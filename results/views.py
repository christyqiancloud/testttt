from django.http import HttpResponse
import datetime

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def correct(request):
    html = "<html><body>You are correct!</body></html>"
    return HttpResponse(html)

def incorrect(request):
    html = "<html><body>You are wrong. Sucks to suck.</body></html>"
    return HttpResponse(html)
