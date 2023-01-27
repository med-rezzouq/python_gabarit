from django.urls import path, re_path
from . import views
urlpatterns = [
path('', views.index),
path('cigma', views.ViewGabarit1),
path('kawtar', views.ViewGabarit2),
path('gabarit3.html', views.ViewGabarit3),
path('gabarit4.html', views.ViewGabarit4),
path('gabarit5.html', views.ViewGabarit5),
path('gabarit6.html', views.ViewGabarit6),
path('ici/<int:X>/', views.redirect_to_autre_URL),
path('test_time_zone.html', views.ViewGabarit5_v2),
path('LesDernieresQuestions', views.dernieres5Questions),
path('LesDernieresQuestionsV2', views.dernieres5QuestionsV2),
path('questions/<int:question_id>/', views.detail),
path('question/<int:question_id>/', views.detailV2, name='detail'),
path('test_get_object_or_404/<int:question_id>/', views.detailV3),
path('test_get_list_or_404/<int:m>/', views.detailV4),
path('testerFormulaireSimpleSansSubmit/<int:question_id>/', views.Question_a_partir_id),
path('testvote/<int:question_id>/', views.voter,name='vote'),
path('testerTroisQuestVueGenerique/', views.IndexView.as_view()),
path('testerDetailView/<int:pk>/', views.DetailView.as_view()),
path('testerListView/', views.QuestionListView.as_view()),


path('testDRF/',views.norest_nomodel),
path('testDRFtest1/',views.norest_from_model),
path('testDRFtest2Choice/',views.get_post_Choice),
path('testDRFtest2Question/',views.get_post_Question),
path('testDRFtest3/<int:pk>/',views.get_delete_put),

]
""" 
    #re_path(r'^date/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/(?P<d>[0-9]{2})/$', views.Viewgabarit9),
"""


from django.urls import path
"""
from . import views
#app_name = 'polls' # masquer ça
urlpatterns = [
path('', views.IndexView.as_view(), name='index'),
path('<int:pk>/', views.DetailView.as_view(), name='detail'),
path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
]"""

