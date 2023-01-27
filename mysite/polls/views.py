from django.http import HttpResponse
def index(request):
	return HttpResponse("Bonjour, vous êtes sur polls index.")
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
def ViewGabarit1(request):
	ch="Bonjour mes chers"
	I=2021
	R=3.14
	template = loader.get_template('polls/gabarit1.html')
	context = {'MaChaine':ch, 'MonInt':I, 'MonRéel':R }
	return HttpResponse(template.render(context,request))


def ViewGabarit2(request):
	L=[2020, "Génie Logiciel", "CIGMA", "Master-M2"]
	template = loader.get_template('polls/gabarit2.html')
	context = {'ifosGLM2':L }
	return HttpResponse(template.render(context,request))

def ViewGabarit3(request):
	ventes = {"Amine": 14, "Rachid": 19, "Hamza": 15}
	template =loader.get_template('polls/gabarit3.html')
	context = {'DictionnaireDesVentes':ventes}
	return HttpResponse(template.render(context,request))

def ViewGabarit4(request):
	 L=[100,200,300,400,500]
	 ch='Bonjour'
	 ventes = {"Amine": 14, "Rachid": 19, "Hamza": 15,
			   "Taha": 21, "Aya": 17}
	 template = loader.get_template('polls/gabarit4.html')
	 context = {'DictionnaireDesVentes':ventes,
				'maListe':L, 'maChaine':ch   }
	 return HttpResponse(template.render(context,request))


def ViewGabarit5(request):
    import datetime
    L=[100,200,300,400,500]
    ch='Bonjour'
    Datecomplete=datetime.datetime.now()
    Annee = Datecomplete.year
    ventes = {"Amine": 14, "Rachid": 19, "Hamza": 15, "Taha": 21, "Aya": 17}
    template = loader.get_template('polls/gabarit5.html')
    context = {'DictionnaireDesVentes':ventes, 'maListe':L, 'maChaine':ch,
               'DateActuelle':Datecomplete, 'Annee':Annee}
    return HttpResponse(template.render(context,request))

def ViewGabarit5_v2(request):
    from django.utils import timezone
    d=timezone.now()
    template = loader.get_template('polls/gabarit5_time_zone.html')
    context = {'DateActuelle':d}
    return HttpResponse(template.render(context,request))

from django.template import engines
django_engine = engines['django']
def ViewGabarit6(request):
    import datetime
    ch='Bonjour'
    Datecomplete=datetime.datetime.now()
    context = {'maChaine':ch,'DateActuelle':Datecomplete}
    template = django_engine.from_string("{{maChaine|add:', '}} <br>Nous somme le:{{ DateActuelle }}!")
    return HttpResponse(template.render(context,request))

from django.utils import timezone
import datetime
def ViewGabarit7(request, N):
    import datetime
    now=datetime.datetime.now()
    DateDecalee=now - datetime.timedelta(days=N)
    template = loader.get_template('polls/gabarit7.html')
    context = {'valeurDeN':N, 'DateAujourdhuit':now,'LaDateDecalee':DateDecalee}
    return HttpResponse(template.render(context, request))


def ViewGabarit8(request, debut, fin, pas,ch):
    L=[200,300,400,500, 1000, 2000,[250,600,800,300,600]]
    template = loader.get_template('polls/gabarit8.html')
    positionMot="Bonjour Mes Chers. Bonne continuation avec Django!".index(ch)
    context = {'ElementsDeListe':L[debut:fin+1:pas], 'pos':positionMot}
    return HttpResponse(template.render(context,request))
from django.urls import reverse
def redirect_to_autre_URL(request, X):
    if X>1000: return HttpResponse ('vous avez saisi un grand entier ! ' )
    else:
        return ViewGabarit7(request,X)
        return HttpResponseRedirect(reverse('URL_des_decalages', args=(X,)))
from datetime import * # à faire au début de fichier une seule fois
def ViewGabarit9(request,year, month, day):
    d = date(int(year), int(month), int(day))
    L=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
    ch="C'est un "+str(L[d.weekday()])
    template = loader.get_template('polls/gabarit9.html')
    context = {'reponse':ch}
    return HttpResponse(template.render(context,request))

def ViewGabarit5_v2(request):
    from django.utils import timezone
    d=timezone.now()
    template = loader.get_template('polls/gabarit5_time_zone.html')
    context = {'DateActuelle':d}
    return HttpResponse(template.render(context,request))

from .models import Choice, Question
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
from polls.models import Question
def Question_a_partir_id(request, question_id):
    Q=Question.objects.get(id=question_id)
    context = {'Q':Q}
    return render(request, 'polls/Nouveaugabarit.html', context)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from polls.models import Question
def voter(request, question_id):
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

from django.http import JsonResponse
def norest_nomodel(request):
    L=[{"id":30,"formation":"M2-GL Casablanca"},
       {"id":40,"formation":"M1-GL Casablanca"},
       {"id":50,"formation":"LP CIGMA"}]
    return JsonResponse(L,safe=False)
    #safe=False pour dire que ce n'est pas de la Base de données
    #pour éviter les serialisers
from .models import *
def norest_from_model(request):
    x=Question.objects.all()
    mareponse={'Mesquestions':list(x.values())}
    return JsonResponse(mareponse)
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import QuestionSerializer,ChoiceSerializer
@api_view(['GET','POST'])
#pour dire je vais utiliser la vue suivante
#en tant que API rest
def get_post_Choice(request):
    if request.method=="GET":
        x=Choice.objects.all()
        Choice_serializer=ChoiceSerializer(x,many=True)
        return Response(Choice_serializer.data)
    if request.method=="POST":
        x=request.data
        Choice_serializer=ChoiceSerializer(data=x)
        if Choice_serializer.is_valid():
            Choice_serializer.save()
            return Response(Choice_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(Choice_serializer.data,status=status.HTTP_400_BAD_REQUEST)


def get_post_Question(request):
    if request.method=="GET":
        x=Question.objects.all()
        question_serializer=QuestionSerializer(x,many=True)
        return Response(question_serializer.data)
    if request.method=="POST":
        x=request.data
        quest_serializer=QuestionSerializer(data=x)
        if quest_serializer.is_valid():
            quest_serializer.save()
            return Response(quest_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(quest_serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
#PUT==> update
def get_delete_put(request,pk):
    try:
        x=Question.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        question_serializer=QuestionSerializer(x)
        return Response(question_serializer.data)
    if request.method=="PUT":
        #x=Question.objects.get(pk=pk)
        quest_serializer=QuestionSerializer(x,data=request.data)
        #x c'est l'ancienne data
        #request.data est les nouvelles données
        if quest_serializer.is_valid():
            quest_serializer.save()
            return Response(quest_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(quest_serializer.data,status=status.HTTP_400_BAD_REQUEST)

    if request.method=="DELETE":
        x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
