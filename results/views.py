from django.http import HttpResponse
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import TemplateDoesNotExist
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import sys
sys.path.append("mysite/polls/views.py")
# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def correct(request):
    html = "<html><body>You are correct!\n<a href='http://localhost:8000/polls/'>Back to polls page?</a></body></html>"
    return HttpResponse(html)

def incorrect(request):
    html = f"<html><body>You are wrong!<a href=http://localhost:8000/polls/1>Try again? </a><br><br><br><a href=http://localhost:8000/results/answer>See answers?</a></body></html>"
    return HttpResponse(html)
def answer(request):
    html = f"<html><body>Answer is: Salt Lake City<a href=http://localhost:8000/polls/1> Go back to poll?</a></body></html>"
    return HttpResponse(html)
