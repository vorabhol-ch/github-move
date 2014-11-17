from django.shortcuts import render
from django.http import HttpResponse
from game_center.models import Category


# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    context_dict = {'boldmessage': "Game Center Champion"}
    return render(request,'game_center/index.html', context_dict)

def about(request):
    return render(request,'game_center/about.html')

