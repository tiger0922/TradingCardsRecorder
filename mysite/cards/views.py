from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Card
from .forms import CardForm

# Create your views here.
def home(request):
    template = loader.get_template('cards/home.html')
    Cardlist = Card.objects.all()
    formlist = [[""]]
    for i in Cardlist:
        form = CardForm(instance=i)
        formlist.append(form)
    cards_list = []
    for i in range(11):
        cards_list.append(Card.objects.all()[i*9:(i+1)*9])
    last_card = Card.objects.all()[99]
    context = {
        'cards_list': cards_list,
        'last_card': last_card,
        'formlist' : formlist
    }
    return HttpResponse(template.render(context, request))

