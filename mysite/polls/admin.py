#"""
#from django.contrib import admin
#from .models import Question,Choice
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']
#admin.site.register(Question,Choice)# QuestionAdmin)
#"""

"""
from django.contrib import admin
from .models import Question
from .models import Choice
admin.site.register(Question)
admin.site.register(Choice)
"""
"""
from django.contrib import admin
from .models import Question
class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text']
admin.site.register(Question,QuestionAdmin)
"""

"""
from django.contrib import admin
from .models import Question
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [ ('Modifier le texte de la question', {'fields': ['question_text']}),
                ('Modifier les informations de la date', {'fields': ['pub_date']}), ]
admin.site.register(Question, QuestionAdmin)

from .models import Choice
admin.site.register(Choice)
"""


"""
from django.contrib import admin
from .models import Choice, Question
class ChoiceInline(admin.TabularInline):#StackedInline):
	model = Choice

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [ ('Modifier le texte de la question', {'fields': ['question_text']}),
	('Date information', {'fields': ['pub_date']}), ]
	inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)
"""


"""
from django.contrib import admin
from .models import Choice, Question
class ChoiceInline(admin.TabularInline):
	model = Choice

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [ ('Modifier le texte de la question', {'fields': ['question_text']}),
	('Date information', {'fields': ['pub_date']}), ]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
admin.site.register(Question, QuestionAdmin)
"""






from django.contrib import admin
"""
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):#(admin.StackedInline)
	model = Choice
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ ('Modifier le texte de la question', {'fields': ['question_text']}),
                  ('Date information', {'fields': ['pub_date']}), ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
"""
from django.contrib import admin
from .models import Question
admin.site.register(Question)

