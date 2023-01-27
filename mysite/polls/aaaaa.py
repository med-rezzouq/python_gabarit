from django.utils import timezone
from polls.models import Choice, Question
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
print(Question.objects.get(id=2))
