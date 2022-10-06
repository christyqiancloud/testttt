# from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
# from django.shortcuts import get_object_or_404, render
# from .models import Choice, Question
# from django.urls import reverse
# from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import TemplateDoesNotExist
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('/usatest/')
    return response

class IndexView(generic.ListView):
    template_name = 'usatest/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'usatest/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist,TemplateDoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'usatest/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        if str(selected_choice) == "Salt Lake City":
            return HttpResponseRedirect("/results/correct")
        else:
            return HttpResponseRedirect("/results/incorrect")


        # print(f"DEBUG: reverse('usatest:results', args=(question.id,)) = {reverse('usatest:results', args=(question.id,))}")

        # return HttpResponseRedirect(reverse('usatest:results', args=(question.id,)))



# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'usatest/index.html', context)



# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'usatest/detail.html', {'question': question})



# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'usatest/results.html', {'question': question})


"""


"""
