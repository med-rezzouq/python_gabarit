
from polls.models import Choice, Question
def detail(request, question_id):
    Q=Question.objects.get(id=question_id)
    contenu=str(Q)
    X=str(question_id)+ '  de contenu = '+contenu
    return HttpResponse("You're looking at question "+X)

def dernieres5Questions(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def dernieres5QuestionsV2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


from django.http import Http404
from django.shortcuts import render

def detailV2(request, question_id):
    try:question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
	    raise Http404("La Question n’existe pas")
    return render(request, 'polls/detail.html', {'question': question})

def detailV3(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

from django.shortcuts import get_list_or_404
def detailV4(request, m):
	questions = get_list_or_404(Question, pk__lte=m)
	return render(request, 'polls/detail4.html', {'questions': questions})

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from polls.models import Question

def AfficherResults(request, question_id):
      question = get_object_or_404(Question, pk=question_id)
      return render(request, 'polls/results.html', {'question': question})

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from polls.models import Question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choixUtilisateur'])
    except (KeyError, Choice.DoesNotExist):
         # Redisplay the question voting form.
        return render(request, 'polls/formulaireVoter.html',{ 'question': question,})
    else:
        selected_choice.votes += 1 ; selected_choice.save()
        return AfficherResultsAvecRelancerVotes(request, question_id)

def testerFormulaire(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/formulaireVoter.html',
                  {'question': question})

def AfficherResultsAvecRelancerVotes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/resultsAvecRelancerProcedureVotes.html', {'question': question})

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from polls.models import Choice, Question
class IndexView(generic.ListView):
    template_name = 'polls/indexGenerique.html'
    context_object_name = 'LesTroisDernieresQuestions'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:3]

class DetailView(generic.DetailView):
    model = Question
    #masquer la ligne ci-dessous pour voir l'effet par défaut
    #template_name = 'polls/Question_detail.html'

class QuestionListView(generic.ListView):
    model = Question
    context_object_name = 'questions'
    queryset = Question.objects.filter(question_text__icontains='vous')
    #template_name = 'polls/Question_list.html'

