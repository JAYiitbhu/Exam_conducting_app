from django import template 
from users.models import Question,Chocies
register = template.Library()


@register.filter()
def get_choices(question):
    return question.objects.filter(question=question)